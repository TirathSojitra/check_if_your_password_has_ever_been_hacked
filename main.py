import requests
import hashlib


def get_data(char):
    url = "https://api.pwnedpasswords.com/range/" + char
    response = requests.get(url)
    if response.status_code == 400:
        return RuntimeError
    else:
        return response


def get_leak_count(our_hash, res_hash):
    # print(our_hash)
    res_hash = res_hash.text.splitlines()
    for item in res_hash:
        if item.split(':')[0] == our_hash:
            return item.split(':')[1]
    return 0


def check_pwd(password):
    encrypted_pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    head_five, tail = encrypted_pass[:5], encrypted_pass[5:]
    temp = get_data(head_five)
    ans = get_leak_count(tail, temp)
    # print(ans)
    return ans


def main():
    f = open("pwd.txt", "r+")
    pwds = list(f.read().split('\n'))
    #print(pwds)
    f.close()

    for items in pwds:
        count = check_pwd(items)
        print(f"Your password \"{items}\" is hacked {count} times")


if __name__ == '__main__':
    main()
