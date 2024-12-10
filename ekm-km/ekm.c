#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>

#include <net/sock.h>
#include <linux/netlink.h>
#include <linux/skbuff.h>

#define EKM_NETLINK 30

struct sock *nl_sk = NULL;

static void recv_msg(struct sk_buff *skb)
{
  printk(KERN_INFO "[EKM] --> Entering in :%s\n", __FUNCTION__);

  struct nlmsghdr *nlhead;
  struct sk_buff *skb_out;
  int pid, res, msg_size;
  char *msg = "Hello, from kenel";

  msg_size = strlen(msg);
  nlhead = (struct nlmsghdr*)skb->data;
  printk(KERN_INFO "[ELM] --> Receive: %s\n", (char*)nlmsg_data(nlhead));
  pid = nlhead->nlmsg_pid;

  skb_out = nlmsg_new(msg_size, 0);
  if(!skb_out)
  {
    printk(KERN_ERR "[ELM] --> Failed to allocate new skb\n");
    return;
  }

  nlhead = nlmsg_put(skb_out, 0, 0, NLMSG_DONE, msg_size, 0);
  NETLINK_CB(skb_out).dst_group = 0;
  strncpy(nlmsg_data(nlhead), msg, msg_size);
  res = nlmsg_unicast(nl_sk, skb_out, pid);

  if(res < 0)
    printk(KERN_INFO "[EKM] --> Error while sending response to user\n");
}

static int __init hello_start(void)
{
  printk(KERN_INFO "[EKM] Loading module ...\n");

  struct netlink_kernel_cfg cfg = {
    .input = recv_msg,
  };
  nl_sk = netlink_kernel_create(&init_net, EKM_NETLINK, &cfg);
  if(!nl_sk) {
    printk(KERN_ALERT "[EKM] Error while creating socket\n");
    return -10;
  }

  printk(KERN_INFO "[EKM] Ekm was successfuly inited!\n");
  return 0;
}

static void __exit hello_end(void)
{
  printk(KERN_INFO "[EKM] Goodbye!\n");
  netlink_kernel_release(nl_sk);
}

module_init(hello_start);
module_exit(hello_end);

MODULE_VERSION("0.1.0");
MODULE_DESCRIPTION("Echo Kernel Module");
MODULE_AUTHOR("Konstantin Freidlin");
MODULE_LICENSE("GPL");

