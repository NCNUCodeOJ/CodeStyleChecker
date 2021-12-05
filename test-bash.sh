docker run -it -v $PWD:/code \
               --tmpfs /tmp \
               --tmpfs /log \
               --env-file $PWD/.env\
               --rm --read-only \
               --cap-drop FSETID \
               --cap-drop MKNOD \
               --cap-drop SETFCAP \
               --cap-drop SETPCAP \
               --cap-drop NET_BIND_SERVICE \
               --cap-drop SYS_CHROOT \
               style_test /bin/bash
