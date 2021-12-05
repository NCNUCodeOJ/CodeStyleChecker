docker run --tmpfs /tmp \
    --tmpfs /log \
    --rm --read-only \
    --cap-drop FSETID \
    --cap-drop MKNOD \
    --cap-drop SETFCAP \
    --cap-drop SETPCAP \
    --cap-drop NET_BIND_SERVICE \
    --cap-drop SYS_CHROOT \
    style_test python3 test.py
