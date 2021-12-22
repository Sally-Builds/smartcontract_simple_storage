from brownie import SimpleStorage, accounts

def test_deploy():
    #Arrange
    account = accounts[0]
    #Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expecteding_value = 0
    #Assert
    assert starting_value == expecteding_value

def test_updating_storage():
    #Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    #Act
    expecting_value = 35
    simple_storage.store(expecting_value, {"from": account})
    #Assert
    assert simple_storage.retrieve() == expecting_value