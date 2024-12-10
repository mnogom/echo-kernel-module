#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>

static int __init hello_start(void)
{
  printk(KERN_INFO "[EKM] Loading module ...\n");
  printk(KERN_INFO "[EKM] Hello, World!\n");
  return 0;
}

static void __exit hello_end(void)
{
  printk(KERN_INFO "[EKM] Goodbye!\n");
}

module_init(hello_start);
module_exit(hello_end);

MODULE_VERSION("0.1.0");
MODULE_DESCRIPTION("Echo Kernel Module");
MODULE_AUTHOR("Konstantin Freidlin");
MODULE_LICENSE("GPL");

