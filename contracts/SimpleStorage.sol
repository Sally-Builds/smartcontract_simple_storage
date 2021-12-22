//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 public numb;
    function store(uint256 fave) public { 
    numb = fave;
}
function retrieve () public view returns(uint256) {
    return numb;
}
}