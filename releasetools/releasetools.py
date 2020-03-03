def FullOTA_InstallEnd(info):
    info.script.AppendExtra('run_program("/sbin/mount", "-t", "auto", "/system");');
    info.script.AppendExtra('run_program("/sbin/sed", "-i", "/exfat/d", "/system/etc/selinux/plat_sepolicy.cil");');
    info.script.AppendExtra('run_program("/sbin/sed", "-i", "/sdfat/d", "/system/etc/selinux/plat_sepolicy.cil");');
    info.script.AppendExtra('run_program("/sbin/umount", "-t", "auto", "/system");');
