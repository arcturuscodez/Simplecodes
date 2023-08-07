*** Settings ***
Library  testlibrary.py

*** Variables ***
${account_name}  test_account

*** Test Cases ***
Test Encryption Key Generation And Saving
    generate_and_save_encryption_key
    load_encryption_key

Test Credentials Generation
    generate_and_save_encryption_key
    generate_credentials  ${account_name}

Test Access With New Encryption Key
    generate_and_save_encryption_key
    generate_credentials  ${account_name}
    generate_and_save_encryption_key
    ${result}  Run Keyword And Return Status  access_credentials  ${account_name}
    Should Be Equal  ${result}  ${False}

Test Generate Credentials Without Encryption Key
    ${result}  Run Keyword And Return Status  generate_credentials  ${account_name}
    Should Be Equal  ${result}  ${False}

Test Access Credentials Without Encryption Key
    ${result}  Run Keyword And Return Status  access_credentials  ${account_name}
    Should Be Equal  ${result}  ${False}

Test Access Credentials With Correct Encryption Key
    generate_and_save_encryption_key
    generate_credentials  ${account_name}
    ${result}  Run Keyword And Return Status  access_credentials  ${account_name}
    Should Be Equal  ${result}  ${True}