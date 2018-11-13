from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = (
    b'gAAAAABb6bzNr5LRGc2MBJxz0cF9EB7_LtOHD9lCwRWuuY2dpdk'
    b'_V7dLZNevNXDaVMrLgacM5ufgEZGhIR2RzxkDZIpJXGDeaeP7JO'
    b'iJvocy1Jw_rW-lIYwvO7tOdcjZL3M1uOy7b0G4RpfME1CgJqdWt'
    b'0Sh8v8etBVMmTw1TpZfX5MGjL6jvuFGcsC-eIB965dbRB7cJerD')

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()