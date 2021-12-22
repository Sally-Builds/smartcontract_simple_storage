from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    #3 ways to add accounts

    #1) Built-in local ganache accounts
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    store_value = simple_storage.retrieve()
    transaction = simple_storage.store(35, {"from": account})
    transaction.wait(1)
    updated_store_value = simple_storage.retrieve()
    print(updated_store_value)
    # print(account)

    # 2) encrypted command line
    # account = accounts.load('freecode_account')
    # print(account)

    #3) environmental variables
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)


def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()