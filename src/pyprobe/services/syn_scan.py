from scapy.all import IP, TCP, sr1, send
import os

def syn_scan(target_ip, port, timeout=3, verbose_status=False):
    if os.name != "nt" and os.getuid() != 0:
        raise PermissionError(
            "SYN scanning requires elevated privileges."
        )

    packet = IP(dst=target_ip) / TCP(dport=port, flags="S")

    response = sr1(packet, timeout=timeout, verbose=0)

    if response is None:
        return None

    if not response.haslayer(TCP):
        return None

    flags = int(response.getlayer(TCP).flags)

    # SYN-ACK: port is open
    if flags & 0x12 == 0x12: # Bitwise check
        if verbose_status:
            print(f"{port}: Open")

        # Reset the half-open TCP connection
        rst_packet = (IP(dst=target_ip)/ TCP(dport=port, flags="R"))
        send(rst_packet, verbose=0)

        return port

    # RST or RST-ACK: port is closed
    if flags & 0x04:
        return None

    return None
