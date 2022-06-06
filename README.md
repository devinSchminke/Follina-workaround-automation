# Follina-workaround-automation
This is a workaround that should secure machines from the Follina zero-day exploit. 
(According to Microsoft's documentation)

https://msrc-blog.microsoft.com/2022/05/30/guidance-for-cve-2022-30190-microsoft-support-diagnostic-tool-vulnerability/

This script will make a new hidden dir on the C:/ drive, that should have a backup of the regkey that will be deleted. 

I did this so once Microsoft patches this, I should be able to come back and re-add the key back and regain the lost functionality. 

Once the backup is done, the code will go on to delete the regkey (reg delete HKEY_CLASSES_ROOT\ms-msdt /f) that microsoft says will secure the machine from the Follina exploit. 


That is all. 
Pretty simple. 
