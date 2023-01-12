Starting Test 1, iterate...
auid=4294967295
interp auid=unset
auid=848
interp auid=unknown(848)
auid=848
interp auid=unknown(848)
Test 1 Done

Starting Test 2, walk events, records, and fields...
event 1 has 1 records
    record 1 of type 1006(LOGIN) has 5 fields
    line=1 file=None
    event time: 1143146623.787:142, host=(null)
        type=LOGIN (LOGIN)
        pid=2027 (2027)
        uid=0 (root)
        auid=4294967295 (unset)
        auid=848 (unknown(848))

event 2 has 1 records
    record 1 of type 1300(SYSCALL) has 24 fields
    line=2 file=None
    event time: 1143146623.875:143, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=188 (setxattr)
        success=yes (yes)
        exit=0 (0)
        a0=7fffffa9a9f0 (0x7fffffa9a9f0)
        a1=3958d11333 (0x3958d11333)
        a2=5131f0 (0x5131f0)
        a3=20 (0x20)
        items=1 (1)
        pid=2027 (2027)
        auid=848 (unknown(848))
        uid=0 (root)
        gid=0 (root)
        euid=0 (root)
        suid=0 (root)
        fsuid=0 (root)
        egid=0 (root)
        sgid=0 (root)
        fsgid=0 (root)
        tty=tty3 (tty3)
        comm="login" (login)
        exe="/bin/login" (/bin/login)
        subj=system_u:system_r:local_login_t:s0-s0:c0.c255 (system_u:system_r:local_login_t:s0-s0:c0.c255)

event 3 has 1 records
    record 1 of type 1112(USER_LOGIN) has 10 fields
    line=3 file=None
    event time: 1143146623.879:146, host=(null)
        type=USER_LOGIN (USER_LOGIN)
        pid=2027 (2027)
        uid=0 (root)
        auid=848 (unknown(848))
        uid=848 (unknown(848))
        exe="/bin/login" (/bin/login)
        hostname=? (?)
        addr=? (?)
        terminal=tty3 (tty3)
        res=success (success)

Test 2 Done

Starting Test 3, walk events, records of 1 buffer...
event has 1 records
    record 1 of type 1112(USER_LOGIN) has 10 fields
    line=1 file=None
    event time: 1143146623.879:146, host=(null)

Test 3 Done

Starting Test 4, walk events, records of 1 file...
event 1 has 4 records
    record 1 of type 1400(AVC) has 11 fields
    line=1 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=AVC (AVC)
        seresult=denied (denied)
        seperms=read,write (read,write)
        pid=13010 (13010)
        comm="pickup" (pickup)
        name="maildrop" (maildrop)
        dev=hda7 (hda7)
        ino=14911367 (14911367)
        scontext=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)
        tcontext=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)
        tclass=dir (dir)

    record 2 of type 1300(SYSCALL) has 26 fields
    line=2 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=2 (open)
        success=no (no)
        exit=-13 (EACCES(Permission denied))
        a0=5555665d91b0 (0x5555665d91b0)
        a1=10800 (O_RDONLY|O_NONBLOCK|O_DIRECTORY)
        a2=5555665d91b8 (0x5555665d91b8)
        a3=0 (0x0)
        items=1 (1)
        ppid=2013 (2013)
        pid=13010 (13010)
        auid=4294967295 (unset)
        uid=890 (unknown(890))
        gid=890 (unknown(890))
        euid=890 (unknown(890))
        suid=890 (unknown(890))
        fsuid=890 (unknown(890))
        egid=890 (unknown(890))
        sgid=890 (unknown(890))
        fsgid=890 (unknown(890))
        tty=(none) ((none))
        comm="pickup" (pickup)
        exe="/usr/libexec/postfix/pickup" (/usr/libexec/postfix/pickup)
        subj=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)
        key=(null) ((null))

    record 3 of type 1307(CWD) has 2 fields
    line=3 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=CWD (CWD)
        cwd="/var/spool/postfix" (/var/spool/postfix)

    record 4 of type 1302(PATH) has 10 fields
    line=4 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=PATH (PATH)
        item=0 (0)
        name="maildrop" (maildrop)
        inode=14911367 (14911367)
        dev=03:07 (03:07)
        mode=040730 (dir,730)
        ouid=890 (unknown(890))
        ogid=891 (unknown(891))
        rdev=00:00 (00:00)
        obj=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)

event 2 has 1 records
    record 1 of type 1101(USER_ACCT) has 11 fields
    line=5 file=test.log
    event time: 1170021601.340:294, host=(null)
        type=USER_ACCT (USER_ACCT)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 3 has 1 records
    record 1 of type 1103(CRED_ACQ) has 11 fields
    line=6 file=test.log
    event time: 1170021601.342:295, host=(null)
        type=CRED_ACQ (CRED_ACQ)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 4 has 1 records
    record 1 of type 1006(LOGIN) has 5 fields
    line=7 file=test.log
    event time: 1170021601.343:296, host=(null)
        type=LOGIN (LOGIN)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        auid=0 (root)

event 5 has 1 records
    record 1 of type 1105(USER_START) has 11 fields
    line=8 file=test.log
    event time: 1170021601.344:297, host=(null)
        type=USER_START (USER_START)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 6 has 1 records
    record 1 of type 1104(CRED_DISP) has 11 fields
    line=9 file=test.log
    event time: 1170021601.364:298, host=(null)
        type=CRED_DISP (CRED_DISP)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 7 has 1 records
    record 1 of type 1106(USER_END) has 11 fields
    line=10 file=test.log
    event time: 1170021601.366:299, host=(null)
        type=USER_END (USER_END)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

Test 4 Done

Starting Test 5, walk events, records of 2 files...
event 1 has 4 records
    record 1 of type 1400(AVC) has 11 fields
    line=1 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=AVC (AVC)
        seresult=denied (denied)
        seperms=read,write (read,write)
        pid=13010 (13010)
        comm="pickup" (pickup)
        name="maildrop" (maildrop)
        dev=hda7 (hda7)
        ino=14911367 (14911367)
        scontext=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)
        tcontext=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)
        tclass=dir (dir)

    record 2 of type 1300(SYSCALL) has 26 fields
    line=2 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=2 (open)
        success=no (no)
        exit=-13 (EACCES(Permission denied))
        a0=5555665d91b0 (0x5555665d91b0)
        a1=10800 (O_RDONLY|O_NONBLOCK|O_DIRECTORY)
        a2=5555665d91b8 (0x5555665d91b8)
        a3=0 (0x0)
        items=1 (1)
        ppid=2013 (2013)
        pid=13010 (13010)
        auid=4294967295 (unset)
        uid=890 (unknown(890))
        gid=890 (unknown(890))
        euid=890 (unknown(890))
        suid=890 (unknown(890))
        fsuid=890 (unknown(890))
        egid=890 (unknown(890))
        sgid=890 (unknown(890))
        fsgid=890 (unknown(890))
        tty=(none) ((none))
        comm="pickup" (pickup)
        exe="/usr/libexec/postfix/pickup" (/usr/libexec/postfix/pickup)
        subj=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)
        key=(null) ((null))

    record 3 of type 1307(CWD) has 2 fields
    line=3 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=CWD (CWD)
        cwd="/var/spool/postfix" (/var/spool/postfix)

    record 4 of type 1302(PATH) has 10 fields
    line=4 file=test.log
    event time: 1170021493.977:293, host=(null)
        type=PATH (PATH)
        item=0 (0)
        name="maildrop" (maildrop)
        inode=14911367 (14911367)
        dev=03:07 (03:07)
        mode=040730 (dir,730)
        ouid=890 (unknown(890))
        ogid=891 (unknown(891))
        rdev=00:00 (00:00)
        obj=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)

event 2 has 1 records
    record 1 of type 1101(USER_ACCT) has 11 fields
    line=5 file=test.log
    event time: 1170021601.340:294, host=(null)
        type=USER_ACCT (USER_ACCT)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 3 has 1 records
    record 1 of type 1103(CRED_ACQ) has 11 fields
    line=6 file=test.log
    event time: 1170021601.342:295, host=(null)
        type=CRED_ACQ (CRED_ACQ)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 4 has 1 records
    record 1 of type 1006(LOGIN) has 5 fields
    line=7 file=test.log
    event time: 1170021601.343:296, host=(null)
        type=LOGIN (LOGIN)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        auid=0 (root)

event 5 has 1 records
    record 1 of type 1105(USER_START) has 11 fields
    line=8 file=test.log
    event time: 1170021601.344:297, host=(null)
        type=USER_START (USER_START)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 6 has 1 records
    record 1 of type 1104(CRED_DISP) has 11 fields
    line=9 file=test.log
    event time: 1170021601.364:298, host=(null)
        type=CRED_DISP (CRED_DISP)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 7 has 1 records
    record 1 of type 1106(USER_END) has 11 fields
    line=10 file=test.log
    event time: 1170021601.366:299, host=(null)
        type=USER_END (USER_END)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 8 has 4 records
    record 1 of type 1400(AVC) has 11 fields
    line=1 file=test2.log
    event time: 1170021493.977:293, host=(null)
        type=AVC (AVC)
        seresult=denied (denied)
        seperms=read (read)
        pid=13010 (13010)
        comm="pickup" (pickup)
        name="maildrop" (maildrop)
        dev=hda7 (hda7)
        ino=14911367 (14911367)
        scontext=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)
        tcontext=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)
        tclass=dir (dir)

    record 2 of type 1300(SYSCALL) has 26 fields
    line=2 file=test2.log
    event time: 1170021493.977:293, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=2 (open)
        success=no (no)
        exit=-13 (EACCES(Permission denied))
        a0=5555665d91b0 (0x5555665d91b0)
        a1=10800 (O_RDONLY|O_NONBLOCK|O_DIRECTORY)
        a2=5555665d91b8 (0x5555665d91b8)
        a3=0 (0x0)
        items=1 (1)
        ppid=2013 (2013)
        pid=13010 (13010)
        auid=4294967295 (unset)
        uid=890 (unknown(890))
        gid=890 (unknown(890))
        euid=890 (unknown(890))
        suid=890 (unknown(890))
        fsuid=890 (unknown(890))
        egid=890 (unknown(890))
        sgid=890 (unknown(890))
        fsgid=890 (unknown(890))
        tty=(none) ((none))
        comm="pickup" (pickup)
        exe="/usr/libexec/postfix/pickup" (/usr/libexec/postfix/pickup)
        subj=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)
        key=(null) ((null))

    record 3 of type 1307(CWD) has 2 fields
    line=3 file=test2.log
    event time: 1170021493.977:293, host=(null)
        type=CWD (CWD)
        cwd="/var/spool/postfix" (/var/spool/postfix)

    record 4 of type 1302(PATH) has 10 fields
    line=4 file=test2.log
    event time: 1170021493.977:293, host=(null)
        type=PATH (PATH)
        item=0 (0)
        name="maildrop" (maildrop)
        inode=14911367 (14911367)
        dev=03:07 (03:07)
        mode=040730 (dir,730)
        ouid=890 (unknown(890))
        ogid=891 (unknown(891))
        rdev=00:00 (00:00)
        obj=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)

event 9 has 1 records
    record 1 of type 1101(USER_ACCT) has 11 fields
    line=5 file=test2.log
    event time: 1170021601.340:294, host=(null)
        type=USER_ACCT (USER_ACCT)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 10 has 1 records
    record 1 of type 1103(CRED_ACQ) has 11 fields
    line=6 file=test2.log
    event time: 1170021601.342:295, host=(null)
        type=CRED_ACQ (CRED_ACQ)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 11 has 1 records
    record 1 of type 1006(LOGIN) has 5 fields
    line=7 file=test2.log
    event time: 1170021601.343:296, host=(null)
        type=LOGIN (LOGIN)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        auid=0 (root)

event 12 has 1 records
    record 1 of type 1105(USER_START) has 11 fields
    line=8 file=test2.log
    event time: 1170021601.344:297, host=(null)
        type=USER_START (USER_START)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 13 has 1 records
    record 1 of type 1104(CRED_DISP) has 11 fields
    line=9 file=test2.log
    event time: 1170021601.364:298, host=(null)
        type=CRED_DISP (CRED_DISP)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 14 has 1 records
    record 1 of type 1106(USER_END) has 11 fields
    line=10 file=test2.log
    event time: 1170021601.366:299, host=(null)
        type=USER_END (USER_END)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

Test 5 Done

Starting Test 6, search...
auid = 500 not found...which is correct
auid exists...which is correct
Testing BUFFER_ARRAY, stop on field
Found auid = 848
Testing BUFFER_ARRAY, stop on record
Found type = SYSCALL
Testing BUFFER_ARRAY, stop on event
Found type = SYSCALL
Testing test.log, stop on field
Found auid = 4294967295
Testing test.log, stop on record
Found type = SYSCALL
Testing test.log, stop on event
Found type = AVC
Test 6 Done

Starting Test 7, compound search...
Found type = USER_START
Found auid = 0
Test 7 Done

Starting Test 8, regex search...
Doing regex match...

Test 8 Done

Starting Test 9, buffer feed...
event 1 has 1 records
    record 1 of type 1006(LOGIN) has 5 fields
    line=1 file=None
    event time: 1143146623.787:142, host=(null)
        type=LOGIN (LOGIN)
        pid=2027 (2027)
        uid=0 (root)
        auid=4294967295 (unset)
        auid=848 (unknown(848))

event 2 has 1 records
    record 1 of type 1300(SYSCALL) has 24 fields
    line=2 file=None
    event time: 1143146623.875:143, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=188 (setxattr)
        success=yes (yes)
        exit=0 (0)
        a0=7fffffa9a9f0 (0x7fffffa9a9f0)
        a1=3958d11333 (0x3958d11333)
        a2=5131f0 (0x5131f0)
        a3=20 (0x20)
        items=1 (1)
        pid=2027 (2027)
        auid=848 (unknown(848))
        uid=0 (root)
        gid=0 (root)
        euid=0 (root)
        suid=0 (root)
        fsuid=0 (root)
        egid=0 (root)
        sgid=0 (root)
        fsgid=0 (root)
        tty=tty3 (tty3)
        comm="login" (login)
        exe="/bin/login" (/bin/login)
        subj=system_u:system_r:local_login_t:s0-s0:c0.c255 (system_u:system_r:local_login_t:s0-s0:c0.c255)

event 3 has 1 records
    record 1 of type 1112(USER_LOGIN) has 10 fields
    line=3 file=None
    event time: 1143146623.879:146, host=(null)
        type=USER_LOGIN (USER_LOGIN)
        pid=2027 (2027)
        uid=0 (root)
        auid=848 (unknown(848))
        uid=848 (unknown(848))
        exe="/bin/login" (/bin/login)
        hostname=? (?)
        addr=? (?)
        terminal=tty3 (tty3)
        res=success (success)

Test 9 Done

Starting Test 10, file feed...
event 1 has 4 records
    record 1 of type 1400(AVC) has 11 fields
    line=1 file=None
    event time: 1170021493.977:293, host=(null)
        type=AVC (AVC)
        seresult=denied (denied)
        seperms=read,write (read,write)
        pid=13010 (13010)
        comm="pickup" (pickup)
        name="maildrop" (maildrop)
        dev=hda7 (hda7)
        ino=14911367 (14911367)
        scontext=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)
        tcontext=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)
        tclass=dir (dir)

    record 2 of type 1300(SYSCALL) has 26 fields
    line=2 file=None
    event time: 1170021493.977:293, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=2 (open)
        success=no (no)
        exit=-13 (EACCES(Permission denied))
        a0=5555665d91b0 (0x5555665d91b0)
        a1=10800 (O_RDONLY|O_NONBLOCK|O_DIRECTORY)
        a2=5555665d91b8 (0x5555665d91b8)
        a3=0 (0x0)
        items=1 (1)
        ppid=2013 (2013)
        pid=13010 (13010)
        auid=4294967295 (unset)
        uid=890 (unknown(890))
        gid=890 (unknown(890))
        euid=890 (unknown(890))
        suid=890 (unknown(890))
        fsuid=890 (unknown(890))
        egid=890 (unknown(890))
        sgid=890 (unknown(890))
        fsgid=890 (unknown(890))
        tty=(none) ((none))
        comm="pickup" (pickup)
        exe="/usr/libexec/postfix/pickup" (/usr/libexec/postfix/pickup)
        subj=system_u:system_r:postfix_pickup_t:s0 (system_u:system_r:postfix_pickup_t:s0)
        key=(null) ((null))

    record 3 of type 1307(CWD) has 2 fields
    line=3 file=None
    event time: 1170021493.977:293, host=(null)
        type=CWD (CWD)
        cwd="/var/spool/postfix" (/var/spool/postfix)

    record 4 of type 1302(PATH) has 10 fields
    line=4 file=None
    event time: 1170021493.977:293, host=(null)
        type=PATH (PATH)
        item=0 (0)
        name="maildrop" (maildrop)
        inode=14911367 (14911367)
        dev=03:07 (03:07)
        mode=040730 (dir,730)
        ouid=890 (unknown(890))
        ogid=891 (unknown(891))
        rdev=00:00 (00:00)
        obj=system_u:object_r:postfix_spool_maildrop_t:s0 (system_u:object_r:postfix_spool_maildrop_t:s0)

event 2 has 1 records
    record 1 of type 1101(USER_ACCT) has 11 fields
    line=5 file=None
    event time: 1170021601.340:294, host=(null)
        type=USER_ACCT (USER_ACCT)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 3 has 1 records
    record 1 of type 1103(CRED_ACQ) has 11 fields
    line=6 file=None
    event time: 1170021601.342:295, host=(null)
        type=CRED_ACQ (CRED_ACQ)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 4 has 1 records
    record 1 of type 1006(LOGIN) has 5 fields
    line=7 file=None
    event time: 1170021601.343:296, host=(null)
        type=LOGIN (LOGIN)
        pid=13015 (13015)
        uid=0 (root)
        auid=4294967295 (unset)
        auid=0 (root)

event 5 has 1 records
    record 1 of type 1105(USER_START) has 11 fields
    line=8 file=None
    event time: 1170021601.344:297, host=(null)
        type=USER_START (USER_START)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 6 has 1 records
    record 1 of type 1104(CRED_DISP) has 11 fields
    line=9 file=None
    event time: 1170021601.364:298, host=(null)
        type=CRED_DISP (CRED_DISP)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

event 7 has 1 records
    record 1 of type 1106(USER_END) has 11 fields
    line=10 file=None
    event time: 1170021601.366:299, host=(null)
        type=USER_END (USER_END)
        pid=13015 (13015)
        uid=0 (root)
        auid=0 (root)
        subj=system_u:system_r:crond_t:s0-s0:c0.c1023 (system_u:system_r:crond_t:s0-s0:c0.c1023)
        acct=root (root)
        exe="/usr/sbin/crond" (/usr/sbin/crond)
        hostname=? (?)
        addr=? (?)
        terminal=cron (cron)
        res=success (success)

Test 10 Done

Starting Test 11, walk LONG event records from a file...
event 1 has 7 records
    record 1 of type 1300(SYSCALL) has 26 fields
    line=1 file=test4.log
    event time: 1655465398.534:25618, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=59 (execve)
        success=yes (yes)
        exit=0 (0)
        a0=8c403a0 (0x8c403a0)
        a1=8c3e8b0 (0x8c3e8b0)
        a2=fffffb6cc5b0 (0xfffffb6cc5b0)
        a3=0 (0x0)
        items=3 (3)
        ppid=105182 (105182)
        pid=105183 (105183)
        auid=573 (unknown(573))
        uid=583 (unknown(583))
        gid=583 (unknown(583))
        euid=583 (unknown(583))
        suid=583 (unknown(583))
        fsuid=583 (unknown(583))
        egid=583 (unknown(583))
        sgid=583 (unknown(583))
        fsgid=583 (unknown(583))
        tty=pts2 (pts2)
        ses=2632 (2632)
        comm="ld" (ld)
        exe="/bin/sh4" (/bin/sh4)
        key=(null) ((null))

    record 2 of type 1309(EXECVE) has 50 fields
    line=2 file=test4.log
    event time: 1655465398.534:25618, host=(null)
        type=EXECVE (EXECVE)
        argc=48 (48)
        a0="/bin/sh" (/bin/sh)
        a1="-efu" (-efu)
        a2="/usr/bin/ld" (/usr/bin/ld)
        a3="-plugin" (-plugin)
        a4="/usr/libexec/gcc/aarch64-alt-linux/8/liblto_plugin.so" (/usr/libexec/gcc/aarch64-alt-linux/8/liblto_plugin.so)
        a5="-plugin-opt=/usr/libexec/gcc/aarch64-alt-linux/8/lto-wrapper" (-plugin-opt=/usr/libexec/gcc/aarch64-alt-linux/8/lto-wrapper)
        a6="-plugin-opt=-fresolution=/usr/src/tmp/cchyHiZN.res" (-plugin-opt=-fresolution=/usr/src/tmp/cchyHiZN.res)
        a7="-plugin-opt=-pass-through=-lgcc" (-plugin-opt=-pass-through=-lgcc)
        a8="-plugin-opt=-pass-through=-lgcc_s" (-plugin-opt=-pass-through=-lgcc_s)
        a9="-plugin-opt=-pass-through=-lc" (-plugin-opt=-pass-through=-lc)
        a10="-plugin-opt=-pass-through=-lgcc" (-plugin-opt=-pass-through=-lgcc)
        a11="-plugin-opt=-pass-through=-lgcc_s" (-plugin-opt=-pass-through=-lgcc_s)
        a12="--build-id" (--build-id)
        a13="--no-add-needed" (--no-add-needed)
        a14="--eh-frame-hdr" (--eh-frame-hdr)
        a15="--hash-style=gnu" (--hash-style=gnu)
        a16="--as-needed" (--as-needed)
        a17="-shared" (-shared)
        a18="-X" (-X)
        a19="-EL" (-EL)
        a20="-maarch64linux" (-maarch64linux)
        a21="-o" (-o)
        a22="ztest105133.so" (ztest105133.so)
        a23="/usr/lib64/gcc/aarch64-alt-linux/8/../../../../lib64/crti.o" (/usr/lib64/gcc/aarch64-alt-linux/8/../../../../lib64/crti.o)
        a24="/usr/lib64/gcc/aarch64-alt-linux/8/crtbeginS.o" (/usr/lib64/gcc/aarch64-alt-linux/8/crtbeginS.o)
        a25="-L/usr/lib64/gcc/aarch64-alt-linux/8" (-L/usr/lib64/gcc/aarch64-alt-linux/8)
        a26="-L/usr/lib64/gcc/aarch64-alt-linux/8/../../../../lib64" (-L/usr/lib64/gcc/aarch64-alt-linux/8/../../../../lib64)
        a27="-L/lib/../lib64" (-L/lib/../lib64)
        a28="-L/usr/lib/../lib64" (-L/usr/lib/../lib64)
        a29="-L/usr/lib64/gcc/aarch64-alt-linux/8/../../.." (-L/usr/lib64/gcc/aarch64-alt-linux/8/../../..)
        a30="-soname" (-soname)
        a31="libz.so.1" (libz.so.1)
        a32="--version-script" (--version-script)
        a33="zlib.map" (zlib.map)
        a34="ztest105133.o" (ztest105133.o)
        a35="-lgcc" (-lgcc)
        a36="--push-state" (--push-state)
        a37="--as-needed" (--as-needed)
        a38="-lgcc_s" (-lgcc_s)
        a39="--pop-state" (--pop-state)
        a40="-lc" (-lc)
        a41="-lgcc" (-lgcc)
        a42="--push-state" (--push-state)
        a43="--as-needed" (--as-needed)
        a44="-lgcc_s" (-lgcc_s)
        a45="--pop-state" (--pop-state)
        a46="/usr/lib64/gcc/aarch64-alt-linux/8/crtendS.o" (/usr/lib64/gcc/aarch64-alt-linux/8/crtendS.o)
        a47="/usr/lib64/gcc/aarch64-alt-linux/8/../../../../lib64/crtn.o" (/usr/lib64/gcc/aarch64-alt-linux/8/../../../../lib64/crtn.o)

    record 3 of type 1307(CWD) has 2 fields
    line=3 file=test4.log
    event time: 1655465398.534:25618, host=(null)
        type=CWD (CWD)
        cwd="/usr/src/RPM/BUILD/zlib-1.2.11-alt1" (/usr/src/RPM/BUILD/zlib-1.2.11-alt1)

    record 4 of type 1302(PATH) has 15 fields
    line=4 file=test4.log
    event time: 1655465398.534:25618, host=(null)
        type=PATH (PATH)
        item=0 (0)
        name="/usr/bin/ld" (/usr/bin/ld)
        inode=40854 (40854)
        dev=00:30 (00:30)
        mode=0100755 (file,755)
        ouid=582 (unknown(582))
        ogid=582 (unknown(582))
        rdev=00:00 (00:00)
        nametype=NORMAL (NORMAL)
        cap_fp=0 (none)
        cap_fi=0 (none)
        cap_fe=0 (0)
        cap_fver=0 (0)
        cap_frootid=0 (0)

    record 5 of type 1302(PATH) has 15 fields
    line=5 file=test4.log
    event time: 1655465398.534:25618, host=(null)
        type=PATH (PATH)
        item=1 (1)
        name="/bin/sh" (/bin/sh)
        inode=33238 (33238)
        dev=00:30 (00:30)
        mode=0100755 (file,755)
        ouid=582 (unknown(582))
        ogid=582 (unknown(582))
        rdev=00:00 (00:00)
        nametype=NORMAL (NORMAL)
        cap_fp=0 (none)
        cap_fi=0 (none)
        cap_fe=0 (0)
        cap_fver=0 (0)
        cap_frootid=0 (0)

    record 6 of type 1302(PATH) has 15 fields
    line=6 file=test4.log
    event time: 1655465398.534:25618, host=(null)
        type=PATH (PATH)
        item=2 (2)
        name="/lib64/ld-linux-aarch64.so.1" (/lib64/ld-linux-aarch64.so.1)
        inode=33874 (33874)
        dev=00:30 (00:30)
        mode=0100755 (file,755)
        ouid=582 (unknown(582))
        ogid=582 (unknown(582))
        rdev=00:00 (00:00)
        nametype=NORMAL (NORMAL)
        cap_fp=0 (none)
        cap_fi=0 (none)
        cap_fe=0 (0)
        cap_fver=0 (0)
        cap_frootid=0 (0)

    record 7 of type 1327(PROCTITLE) has 2 fields
    line=7 file=test4.log
    event time: 1655465398.534:25618, host=(null)
        type=PROCTITLE (PROCTITLE)
        proctitle=2F62696E2F7368002D656675002F7573722F62696E2F6C64002D706C7567696E002F7573722F6C6962657865632F6763632F616172636836342D616C742D6C696E75782F382F6C69626C746F5F706C7567696E2E736F002D706C7567696E2D6F70743D2F7573722F6C6962657865632F6763632F616172636836342D616C742D (/bin/sh -efu /usr/bin/ld -plugin /usr/libexec/gcc/aarch64-alt-linux/8/liblto_plugin.so -plugin-opt=/usr/libexec/gcc/aarch64-alt-)

event 2 has 6 records
    record 1 of type 1300(SYSCALL) has 26 fields
    line=8 file=test4.log
    event time: 1655465404.819:27091, host=(null)
        type=SYSCALL (SYSCALL)
        arch=c000003e (x86_64)
        syscall=59 (execve)
        success=yes (yes)
        exit=0 (0)
        a0=1a407f50 (0x1a407f50)
        a1=1a401cd0 (0x1a401cd0)
        a2=1a3ed090 (0x1a3ed090)
        a3=0 (0x0)
        items=2 (2)
        ppid=105932 (105932)
        pid=105933 (105933)
        auid=573 (unknown(573))
        uid=583 (unknown(583))
        gid=583 (unknown(583))
        euid=583 (unknown(583))
        suid=583 (unknown(583))
        fsuid=583 (unknown(583))
        egid=583 (unknown(583))
        sgid=583 (unknown(583))
        fsgid=583 (unknown(583))
        tty=pts2 (pts2)
        ses=2632 (2632)
        comm="m4" (m4)
        exe="/usr/bin/m4" (/usr/bin/m4)
        key=(null) ((null))

    record 2 of type 1309(EXECVE) has 218 fields
    line=9 file=test4.log
    event time: 1655465404.819:27091, host=(null)
        type=EXECVE (EXECVE)
        argc=216 (216)
        a0="/usr/bin/m4" (/usr/bin/m4)
        a1="--nesting-limit=1024" (--nesting-limit=1024)
        a2="--gnu" (--gnu)
        a3="--include=/usr/share/autoconf-2.60" (--include=/usr/share/autoconf-2.60)
        a4="--debug=aflq" (--debug=aflq)
        a5="--fatal-warning" (--fatal-warning)
        a6="--debugfile=autom4te.cache/traces.0t" (--debugfile=autom4te.cache/traces.0t)
        a7="--trace=AC_CHECK_LIBM" (--trace=AC_CHECK_LIBM)
        a8="--trace=AC_CONFIG_MACRO_DIR" (--trace=AC_CONFIG_MACRO_DIR)
        a9="--trace=AC_CONFIG_MACRO_DIR_TRACE" (--trace=AC_CONFIG_MACRO_DIR_TRACE)
        a10="--trace=AC_DEFUN" (--trace=AC_DEFUN)
        a11="--trace=AC_DEFUN_ONCE" (--trace=AC_DEFUN_ONCE)
        a12="--trace=AC_DEPLIBS_CHECK_METHOD" (--trace=AC_DEPLIBS_CHECK_METHOD)
        a13="--trace=AC_DISABLE_FAST_INSTALL" (--trace=AC_DISABLE_FAST_INSTALL)
        a14="--trace=AC_DISABLE_SHARED" (--trace=AC_DISABLE_SHARED)
        a15="--trace=AC_DISABLE_STATIC" (--trace=AC_DISABLE_STATIC)
        a16="--trace=AC_ENABLE_FAST_INSTALL" (--trace=AC_ENABLE_FAST_INSTALL)
        a17="--trace=AC_ENABLE_SHARED" (--trace=AC_ENABLE_SHARED)
        a18="--trace=AC_ENABLE_STATIC" (--trace=AC_ENABLE_STATIC)
        a19="--trace=AC_LIBLTDL_CONVENIENCE" (--trace=AC_LIBLTDL_CONVENIENCE)
        a20="--trace=AC_LIBLTDL_INSTALLABLE" (--trace=AC_LIBLTDL_INSTALLABLE)
        a21="--trace=AC_LIBTOOL_COMPILER_OPTION" (--trace=AC_LIBTOOL_COMPILER_OPTION)
        a22="--trace=AC_LIBTOOL_CONFIG" (--trace=AC_LIBTOOL_CONFIG)
        a23="--trace=AC_LIBTOOL_CXX" (--trace=AC_LIBTOOL_CXX)
        a24="--trace=AC_LIBTOOL_DLOPEN" (--trace=AC_LIBTOOL_DLOPEN)
        a25="--trace=AC_LIBTOOL_DLOPEN_SELF" (--trace=AC_LIBTOOL_DLOPEN_SELF)
        a26="--trace=AC_LIBTOOL_F77" (--trace=AC_LIBTOOL_F77)
        a27="--trace=AC_LIBTOOL_FC" (--trace=AC_LIBTOOL_FC)
        a28="--trace=AC_LIBTOOL_GCJ" (--trace=AC_LIBTOOL_GCJ)
        a29="--trace=AC_LIBTOOL_LANG_CXX_CONFIG" (--trace=AC_LIBTOOL_LANG_CXX_CONFIG)
        a30="--trace=AC_LIBTOOL_LANG_C_CONFIG" (--trace=AC_LIBTOOL_LANG_C_CONFIG)
        a31="--trace=AC_LIBTOOL_LANG_F77_CONFIG" (--trace=AC_LIBTOOL_LANG_F77_CONFIG)
        a32="--trace=AC_LIBTOOL_LANG_GCJ_CONFIG" (--trace=AC_LIBTOOL_LANG_GCJ_CONFIG)
        a33="--trace=AC_LIBTOOL_LANG_RC_CONFIG" (--trace=AC_LIBTOOL_LANG_RC_CONFIG)
        a34="--trace=AC_LIBTOOL_LINKER_OPTION" (--trace=AC_LIBTOOL_LINKER_OPTION)
        a35="--trace=AC_LIBTOOL_OBJDIR" (--trace=AC_LIBTOOL_OBJDIR)
        a36="--trace=AC_LIBTOOL_PICMODE" (--trace=AC_LIBTOOL_PICMODE)
        a37="--trace=AC_LIBTOOL_POSTDEP_PREDEP" (--trace=AC_LIBTOOL_POSTDEP_PREDEP)
        a38="--trace=AC_LIBTOOL_PROG_CC_C_O" (--trace=AC_LIBTOOL_PROG_CC_C_O)
        a39="--trace=AC_LIBTOOL_PROG_COMPILER_NO_RTTI" (--trace=AC_LIBTOOL_PROG_COMPILER_NO_RTTI)
        a40="--trace=AC_LIBTOOL_PROG_COMPILER_PIC" (--trace=AC_LIBTOOL_PROG_COMPILER_PIC)
        a41="--trace=AC_LIBTOOL_PROG_LD_HARDCODE_LIBPATH" (--trace=AC_LIBTOOL_PROG_LD_HARDCODE_LIBPATH)
        a42="--trace=AC_LIBTOOL_PROG_LD_SHLIBS" (--trace=AC_LIBTOOL_PROG_LD_SHLIBS)
        a43="--trace=AC_LIBTOOL_RC" (--trace=AC_LIBTOOL_RC)
        a44="--trace=AC_LIBTOOL_SETUP" (--trace=AC_LIBTOOL_SETUP)
        a45="--trace=AC_LIBTOOL_SYS_DYNAMIC_LINKER" (--trace=AC_LIBTOOL_SYS_DYNAMIC_LINKER)
        a46="--trace=AC_LIBTOOL_SYS_GLOBAL_SYMBOL_PIPE" (--trace=AC_LIBTOOL_SYS_GLOBAL_SYMBOL_PIPE)
        a47="--trace=AC_LIBTOOL_SYS_HARD_LINK_LOCKS" (--trace=AC_LIBTOOL_SYS_HARD_LINK_LOCKS)
        a48="--trace=AC_LIBTOOL_SYS_LIB_STRIP" (--trace=AC_LIBTOOL_SYS_LIB_STRIP)
        a49="--trace=AC_LIBTOOL_SYS_MAX_CMD_LEN" (--trace=AC_LIBTOOL_SYS_MAX_CMD_LEN)
        a50="--trace=AC_LIBTOOL_SYS_OLD_ARCHIVE" (--trace=AC_LIBTOOL_SYS_OLD_ARCHIVE)
        a51="--trace=AC_LIBTOOL_WIN32_DLL" (--trace=AC_LIBTOOL_WIN32_DLL)
        a52="--trace=AC_LIB_LTDL" (--trace=AC_LIB_LTDL)
        a53="--trace=AC_LTDL_DLLIB" (--trace=AC_LTDL_DLLIB)
        a54="--trace=AC_LTDL_DLSYM_USCORE" (--trace=AC_LTDL_DLSYM_USCORE)
        a55="--trace=AC_LTDL_ENABLE_INSTALL" (--trace=AC_LTDL_ENABLE_INSTALL)
        a56="--trace=AC_LTDL_OBJDIR" (--trace=AC_LTDL_OBJDIR)
        a57="--trace=AC_LTDL_PREOPEN" (--trace=AC_LTDL_PREOPEN)
        a58="--trace=AC_LTDL_SHLIBEXT" (--trace=AC_LTDL_SHLIBEXT)
        a59="--trace=AC_LTDL_SHLIBPATH" (--trace=AC_LTDL_SHLIBPATH)
        a60="--trace=AC_LTDL_SYMBOL_USCORE" (--trace=AC_LTDL_SYMBOL_USCORE)
        a61="--trace=AC_LTDL_SYSSEARCHPATH" (--trace=AC_LTDL_SYSSEARCHPATH)
        a62="--trace=AC_LTDL_SYS_DLOPEN_DEPLIBS" (--trace=AC_LTDL_SYS_DLOPEN_DEPLIBS)
        a63="--trace=AC_PATH_MAGIC" (--trace=AC_PATH_MAGIC)
        a64="--trace=AC_PATH_TOOL_PREFIX" (--trace=AC_PATH_TOOL_PREFIX)
        a65="--trace=AC_PROG_EGREP" (--trace=AC_PROG_EGREP)
        a66="--trace=AC_PROG_LD" (--trace=AC_PROG_LD)
        a67="--trace=AC_PROG_LD_GNU" (--trace=AC_PROG_LD_GNU)
        a68="--trace=AC_PROG_LD_RELOAD_FLAG" (--trace=AC_PROG_LD_RELOAD_FLAG)
        a69="--trace=AC_PROG_LIBTOOL" (--trace=AC_PROG_LIBTOOL)
        a70="--trace=AC_PROG_NM" (--trace=AC_PROG_NM)
        a71="--trace=AC_WITH_LTDL" (--trace=AC_WITH_LTDL)
        a72="--trace=AM_AUTOMAKE_VERSION" (--trace=AM_AUTOMAKE_VERSION)
        a73="--trace=AM_AUX_DIR_EXPAND" (--trace=AM_AUX_DIR_EXPAND)
        a74="--trace=AM_CONDITIONAL" (--trace=AM_CONDITIONAL)
        a75="--trace=AM_DEP_TRACK" (--trace=AM_DEP_TRACK)
        a76="--trace=AM_DISABLE_SHARED" (--trace=AM_DISABLE_SHARED)
        a77="--trace=AM_DISABLE_STATIC" (--trace=AM_DISABLE_STATIC)
        a78="--trace=AM_ENABLE_SHARED" (--trace=AM_ENABLE_SHARED)
        a79="--trace=AM_ENABLE_STATIC" (--trace=AM_ENABLE_STATIC)
        a80="--trace=AM_INIT_AUTOMAKE" (--trace=AM_INIT_AUTOMAKE)
        a81="--trace=AM_MAKE_INCLUDE" (--trace=AM_MAKE_INCLUDE)
        a82="--trace=AM_MISSING_HAS_RUN" (--trace=AM_MISSING_HAS_RUN)
        a83="--trace=AM_MISSING_PROG" (--trace=AM_MISSING_PROG)
        a84="--trace=AM_OUTPUT_DEPENDENCY_COMMANDS" (--trace=AM_OUTPUT_DEPENDENCY_COMMANDS)
        a85="--trace=AM_PROG_CC_C_O" (--trace=AM_PROG_CC_C_O)
        a86="--trace=AM_PROG_INSTALL_SH" (--trace=AM_PROG_INSTALL_SH)
        a87="--trace=AM_PROG_INSTALL_STRIP" (--trace=AM_PROG_INSTALL_STRIP)
        a88="--trace=AM_PROG_LD" (--trace=AM_PROG_LD)
        a89="--trace=AM_PROG_LIBTOOL" (--trace=AM_PROG_LIBTOOL)
        a90="--trace=AM_PROG_NM" (--trace=AM_PROG_NM)
        a91="--trace=AM_RUN_LOG" (--trace=AM_RUN_LOG)
        a92="--trace=AM_SANITY_CHECK" (--trace=AM_SANITY_CHECK)
        a93="--trace=AM_SET_CURRENT_AUTOMAKE_VERSION" (--trace=AM_SET_CURRENT_AUTOMAKE_VERSION)
        a94="--trace=AM_SET_DEPDIR" (--trace=AM_SET_DEPDIR)
        a95="--trace=AM_SET_LEADING_DOT" (--trace=AM_SET_LEADING_DOT)
        a96="--trace=AM_SILENT_RULES" (--trace=AM_SILENT_RULES)
        a97="--trace=AM_SUBST_NOTMAKE" (--trace=AM_SUBST_NOTMAKE)
        a98="--trace=AU_DEFUN" (--trace=AU_DEFUN)
        a99="--trace=LTDL_CONVENIENCE" (--trace=LTDL_CONVENIENCE)
        a100="--trace=LTDL_INIT" (--trace=LTDL_INIT)
        a101="--trace=LTDL_INSTALLABLE" (--trace=LTDL_INSTALLABLE)
        a102="--trace=LTOBSOLETE_VERSION" (--trace=LTOBSOLETE_VERSION)
        a103="--trace=LTOPTIONS_VERSION" (--trace=LTOPTIONS_VERSION)
        a104="--trace=LTSUGAR_VERSION" (--trace=LTSUGAR_VERSION)
        a105="--trace=LTVERSION_VERSION" (--trace=LTVERSION_VERSION)
        a106="--trace=LT_AC_PROG_EGREP" (--trace=LT_AC_PROG_EGREP)
        a107="--trace=LT_AC_PROG_GCJ" (--trace=LT_AC_PROG_GCJ)
        a108="--trace=LT_AC_PROG_RC" (--trace=LT_AC_PROG_RC)
        a109="--trace=LT_AC_PROG_SED" (--trace=LT_AC_PROG_SED)
        a110="--trace=LT_CMD_MAX_LEN" (--trace=LT_CMD_MAX_LEN)
        a111="--trace=LT_CONFIG_LTDL_DIR" (--trace=LT_CONFIG_LTDL_DIR)
        a112="--trace=LT_FUNC_ARGZ" (--trace=LT_FUNC_ARGZ)
        a113="--trace=LT_FUNC_DLSYM_USCORE" (--trace=LT_FUNC_DLSYM_USCORE)
        a114="--trace=LT_INIT" (--trace=LT_INIT)
        a115="--trace=LT_LANG" (--trace=LT_LANG)
        a116="--trace=LT_LIB_DLLOAD" (--trace=LT_LIB_DLLOAD)
        a117="--trace=LT_LIB_M" (--trace=LT_LIB_M)
        a118="--trace=LT_OUTPUT" (--trace=LT_OUTPUT)
        a119="--trace=LT_PATH_LD" (--trace=LT_PATH_LD)
        a120="--trace=LT_PATH_NM" (--trace=LT_PATH_NM)
        a121="--trace=LT_PROG_GCJ" (--trace=LT_PROG_GCJ)
        a122="--trace=LT_PROG_GO" (--trace=LT_PROG_GO)
        a123="--trace=LT_PROG_RC" (--trace=LT_PROG_RC)
        a124="--trace=LT_SUPPORTED_TAG" (--trace=LT_SUPPORTED_TAG)
        a125="--trace=LT_SYS_DLOPEN_DEPLIBS" (--trace=LT_SYS_DLOPEN_DEPLIBS)
        a126="--trace=LT_SYS_DLOPEN_SELF" (--trace=LT_SYS_DLOPEN_SELF)
        a127="--trace=LT_SYS_DLSEARCH_PATH" (--trace=LT_SYS_DLSEARCH_PATH)
        a128="--trace=LT_SYS_MODULE_EXT" (--trace=LT_SYS_MODULE_EXT)
        a129="--trace=LT_SYS_MODULE_PATH" (--trace=LT_SYS_MODULE_PATH)
        a130="--trace=LT_SYS_SYMBOL_USCORE" (--trace=LT_SYS_SYMBOL_USCORE)
        a131="--trace=LT_WITH_LTDL" (--trace=LT_WITH_LTDL)
        a132="--trace=_AC_AM_CONFIG_HEADER_HOOK" (--trace=_AC_AM_CONFIG_HEADER_HOOK)
        a133="--trace=_AC_PROG_LIBTOOL" (--trace=_AC_PROG_LIBTOOL)
        a134="--trace=_AM_AUTOCONF_VERSION" (--trace=_AM_AUTOCONF_VERSION)
        a135="--trace=_AM_CONFIG_MACRO_DIRS" (--trace=_AM_CONFIG_MACRO_DIRS)
        a136="--trace=_AM_DEPENDENCIES" (--trace=_AM_DEPENDENCIES)
        a137="--trace=_AM_IF_OPTION" (--trace=_AM_IF_OPTION)
        a138="--trace=_AM_MANGLE_OPTION" (--trace=_AM_MANGLE_OPTION)
        a139="--trace=_AM_OUTPUT_DEPENDENCY_COMMANDS" (--trace=_AM_OUTPUT_DEPENDENCY_COMMANDS)
        a140="--trace=_AM_PROG_CC_C_O" (--trace=_AM_PROG_CC_C_O)
        a141="--trace=_AM_PROG_TAR" (--trace=_AM_PROG_TAR)
        a142="--trace=_AM_SET_OPTION" (--trace=_AM_SET_OPTION)
        a143="--trace=_AM_SET_OPTIONS" (--trace=_AM_SET_OPTIONS)
        a144="--trace=_AM_SUBST_NOTMAKE" (--trace=_AM_SUBST_NOTMAKE)
        a145="--trace=_LTDL_SETUP" (--trace=_LTDL_SETUP)
        a146="--trace=_LT_AC_CHECK_DLFCN" (--trace=_LT_AC_CHECK_DLFCN)
        a147="--trace=_LT_AC_FILE_LTDLL_C" (--trace=_LT_AC_FILE_LTDLL_C)
        a148="--trace=_LT_AC_LANG_CXX" (--trace=_LT_AC_LANG_CXX)
        a149="--trace=_LT_AC_LANG_CXX_CONFIG" (--trace=_LT_AC_LANG_CXX_CONFIG)
        a150="--trace=_LT_AC_LANG_C_CONFIG" (--trace=_LT_AC_LANG_C_CONFIG)
        a151="--trace=_LT_AC_LANG_F77" (--trace=_LT_AC_LANG_F77)
        a152="--trace=_LT_AC_LANG_F77_CONFIG" (--trace=_LT_AC_LANG_F77_CONFIG)
        a153="--trace=_LT_AC_LANG_GCJ" (--trace=_LT_AC_LANG_GCJ)
        a154="--trace=_LT_AC_LANG_GCJ_CONFIG" (--trace=_LT_AC_LANG_GCJ_CONFIG)
        a155="--trace=_LT_AC_LANG_RC_CONFIG" (--trace=_LT_AC_LANG_RC_CONFIG)
        a156="--trace=_LT_AC_LOCK" (--trace=_LT_AC_LOCK)
        a157="--trace=_LT_AC_PROG_CXXCPP" (--trace=_LT_AC_PROG_CXXCPP)
        a158="--trace=_LT_AC_PROG_ECHO_BACKSLASH" (--trace=_LT_AC_PROG_ECHO_BACKSLASH)
        a159="--trace=_LT_AC_SHELL_INIT" (--trace=_LT_AC_SHELL_INIT)
        a160="--trace=_LT_AC_SYS_COMPILER" (--trace=_LT_AC_SYS_COMPILER)
        a161="--trace=_LT_AC_SYS_LIBPATH_AIX" (--trace=_LT_AC_SYS_LIBPATH_AIX)
        a162="--trace=_LT_AC_TAGCONFIG" (--trace=_LT_AC_TAGCONFIG)
        a163="--trace=_LT_AC_TAGVAR" (--trace=_LT_AC_TAGVAR)
        a164="--trace=_LT_AC_TRY_DLOPEN_SELF" (--trace=_LT_AC_TRY_DLOPEN_SELF)
        a165="--trace=_LT_CC_BASENAME" (--trace=_LT_CC_BASENAME)
        a166="--trace=_LT_COMPILER_BOILERPLATE" (--trace=_LT_COMPILER_BOILERPLATE)
        a167="--trace=_LT_COMPILER_OPTION" (--trace=_LT_COMPILER_OPTION)
        a168="--trace=_LT_DLL_DEF_P" (--trace=_LT_DLL_DEF_P)
        a169="--trace=_LT_LIBOBJ" (--trace=_LT_LIBOBJ)
        a170="--trace=_LT_LINKER_BOILERPLATE" (--trace=_LT_LINKER_BOILERPLATE)
        a171="--trace=_LT_LINKER_OPTION" (--trace=_LT_LINKER_OPTION)
        a172="--trace=_LT_PATH_TOOL_PREFIX" (--trace=_LT_PATH_TOOL_PREFIX)
        a173="--trace=_LT_PREPARE_SED_QUOTE_VARS" (--trace=_LT_PREPARE_SED_QUOTE_VARS)
        a174="--trace=_LT_PROG_CXX" (--trace=_LT_PROG_CXX)
        a175="--trace=_LT_PROG_ECHO_BACKSLASH" (--trace=_LT_PROG_ECHO_BACKSLASH)
        a176="--trace=_LT_PROG_F77" (--trace=_LT_PROG_F77)
        a177="--trace=_LT_PROG_FC" (--trace=_LT_PROG_FC)
        a178="--trace=_LT_PROG_LTMAIN" (--trace=_LT_PROG_LTMAIN)
        a179="--trace=_LT_REQUIRED_DARWIN_CHECKS" (--trace=_LT_REQUIRED_DARWIN_CHECKS)
        a180="--trace=_LT_WITH_SYSROOT" (--trace=_LT_WITH_SYSROOT)
        a181="--trace=_m4_warn" (--trace=_m4_warn)
        a182="--trace=include" (--trace=include)
        a183="--trace=m4_include" (--trace=m4_include)
        a184="--trace=m4_pattern_allow" (--trace=m4_pattern_allow)
        a185="--trace=m4_pattern_forbid" (--trace=m4_pattern_forbid)
        a186="--reload-state=/usr/share/autoconf-2.60/autoconf/autoconf.m4f" (--reload-state=/usr/share/autoconf-2.60/autoconf/autoconf.m4f)
        a187="--undefine=__m4_version__" (--undefine=__m4_version__)
        a188="-" (-)
        a189="/usr/share/aclocal-1.16/internal/ac-config-macro-dirs.m4" (/usr/share/aclocal-1.16/internal/ac-config-macro-dirs.m4)
        a190="/usr/share/libtool/aclocal/libtool.m4" (/usr/share/libtool/aclocal/libtool.m4)
        a191="/usr/share/libtool/aclocal/ltargz.m4" (/usr/share/libtool/aclocal/ltargz.m4)
        a192="/usr/share/libtool/aclocal/ltdl.m4" (/usr/share/libtool/aclocal/ltdl.m4)
        a193="/usr/share/libtool/aclocal/ltoptions.m4" (/usr/share/libtool/aclocal/ltoptions.m4)
        a194="/usr/share/libtool/aclocal/ltsugar.m4" (/usr/share/libtool/aclocal/ltsugar.m4)
        a195="/usr/share/libtool/aclocal/ltversion.m4" (/usr/share/libtool/aclocal/ltversion.m4)
        a196="/usr/share/libtool/aclocal/lt~obsolete.m4" (/usr/share/libtool/aclocal/lt~obsolete.m4)
        a197="/usr/share/aclocal-1.16/amversion.m4" (/usr/share/aclocal-1.16/amversion.m4)
        a198="/usr/share/aclocal-1.16/auxdir.m4" (/usr/share/aclocal-1.16/auxdir.m4)
        a199="/usr/share/aclocal-1.16/cond.m4" (/usr/share/aclocal-1.16/cond.m4)
        a200="/usr/share/aclocal-1.16/depend.m4" (/usr/share/aclocal-1.16/depend.m4)
        a201="/usr/share/aclocal-1.16/depout.m4" (/usr/share/aclocal-1.16/depout.m4)
        a202="/usr/share/aclocal-1.16/init.m4" (/usr/share/aclocal-1.16/init.m4)
        a203="/usr/share/aclocal-1.16/install-sh.m4" (/usr/share/aclocal-1.16/install-sh.m4)
        a204="/usr/share/aclocal-1.16/lead-dot.m4" (/usr/share/aclocal-1.16/lead-dot.m4)
        a205="/usr/share/aclocal-1.16/make.m4" (/usr/share/aclocal-1.16/make.m4)
        a206="/usr/share/aclocal-1.16/missing.m4" (/usr/share/aclocal-1.16/missing.m4)
        a207="/usr/share/aclocal-1.16/options.m4" (/usr/share/aclocal-1.16/options.m4)
        a208="/usr/share/aclocal-1.16/prog-cc-c-o.m4" (/usr/share/aclocal-1.16/prog-cc-c-o.m4)
        a209="/usr/share/aclocal-1.16/runlog.m4" (/usr/share/aclocal-1.16/runlog.m4)
        a210="/usr/share/aclocal-1.16/sanity.m4" (/usr/share/aclocal-1.16/sanity.m4)
        a211="/usr/share/aclocal-1.16/silent.m4" (/usr/share/aclocal-1.16/silent.m4)
        a212="/usr/share/aclocal-1.16/strip.m4" (/usr/share/aclocal-1.16/strip.m4)
        a213="/usr/share/aclocal-1.16/substnot.m4" (/usr/share/aclocal-1.16/substnot.m4)
        a214="/usr/share/aclocal-1.16/tar.m4" (/usr/share/aclocal-1.16/tar.m4)
        a215="configure.ac" (configure.ac)

    record 3 of type 1307(CWD) has 2 fields
    line=10 file=test4.log
    event time: 1655465404.819:27091, host=(null)
        type=CWD (CWD)
        cwd="/usr/src/RPM/BUILD/zlib-1.2.11-alt1/contrib/minizip" (/usr/src/RPM/BUILD/zlib-1.2.11-alt1/contrib/minizip)

    record 4 of type 1302(PATH) has 15 fields
    line=11 file=test4.log
    event time: 1655465404.819:27091, host=(null)
        type=PATH (PATH)
        item=0 (0)
        name="/usr/bin/m4" (/usr/bin/m4)
        inode=40839 (40839)
        dev=00:30 (00:30)
        mode=0100755 (file,755)
        ouid=582 (unknown(582))
        ogid=582 (unknown(582))
        rdev=00:00 (00:00)
        nametype=NORMAL (NORMAL)
        cap_fp=0 (none)
        cap_fi=0 (none)
        cap_fe=0 (0)
        cap_fver=0 (0)
        cap_frootid=0 (0)

    record 5 of type 1302(PATH) has 15 fields
    line=12 file=test4.log
    event time: 1655465404.819:27091, host=(null)
        type=PATH (PATH)
        item=1 (1)
        name="/lib64/ld-linux-aarch64.so.1" (/lib64/ld-linux-aarch64.so.1)
        inode=33874 (33874)
        dev=00:30 (00:30)
        mode=0100755 (file,755)
        ouid=582 (unknown(582))
        ogid=582 (unknown(582))
        rdev=00:00 (00:00)
        nametype=NORMAL (NORMAL)
        cap_fp=0 (none)
        cap_fi=0 (none)
        cap_fe=0 (0)
        cap_fver=0 (0)
        cap_frootid=0 (0)

    record 6 of type 1327(PROCTITLE) has 2 fields
    line=13 file=test4.log
    event time: 1655465404.819:27091, host=(null)
        type=PROCTITLE (PROCTITLE)
        proctitle=2F7573722F62696E2F6D34002D2D6E657374696E672D6C696D69743D31303234002D2D676E75002D2D696E636C7564653D2F7573722F73686172652F6175746F636F6E662D322E3630002D2D64656275673D61666C71002D2D666174616C2D7761726E696E67002D2D646562756766696C653D6175746F6D3474652E63616368 (/usr/bin/m4 --nesting-limit=1024 --gnu --include=/usr/share/autoconf-2.60 --debug=aflq --fatal-warning --debugfile=autom4te.cach)

Test 11 Done

Finished non-admin tests

