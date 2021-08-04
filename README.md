# BUGSS_Data_Interface

## An interface to manipulate and view BUGSS data

Click either image to run:

[![Binder](https://bugssonline.org/wp-content/themes/BUGS3/assets/images/bugsslogo-square300.png)](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface.ipynb%3Fvoila-theme%3Ddark)
[![Binder](https://raw.githubusercontent.com/24-Tony/BUGSS_Interface/main/InterfaceQR.png)](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface.ipynb)

### Version History:

**All Versions prior to 0.7.5 have major functional issues and cannot plot and 1.0.0 is the first fully functional version - * designates a pre-release**


| Version  | DARK THEME | LIGHT THEME | Known Bugs |
|:---------|:-----------|:------------|:-----------|
| V 1.2.0: | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%201.2.0.ipynb%3Fvoila-theme%3Ddark) | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%201.2.0.ipynb) | No |
| V 1.1.0: | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%201.1.0.ipynb%3Fvoila-theme%3Ddark) | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%201.1.0.ipynb) | No |
| V 1.0.1: | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%201.0.1.ipynb%3Fvoila-theme%3Ddark) | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%201.0.1.ipynb) | No |
| V 1.0.0: | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%201.0.0.ipynb%3Fvoila-theme%3Ddark) | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%201.0.0.ipynb) | Yes |
| *V 0.7.5: | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%200.7.5.ipynb%3Fvoila-theme%3Ddark) | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%200.7.5.ipynb) | Yes |
| *V 0.5.0: | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%200.5.0.ipynb%3Fvoila-theme%3Ddark) | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%200.5.0.ipynb) | Yes |
| *V 0.2.5: | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%200.2.5.ipynb%3Fvoila-theme%3Ddark) | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%200.2.5.ipynb) | Yes |
| *V 0.1.1: | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%200.1.1.ipynb%3Fvoila-theme%3Ddark) | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%200.1.1.ipynb) | Yes |
| Updating: | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface.ipynb%3Fvoila-theme%3Ddark) | [Run](https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface.ipynb) | Yes |


LATEST RELEASE:

```
https://mybinder.org/v2/gh/24-Tony/BUGSS_Interface/HEAD?urlpath=%2Fvoila%2Frender%2FInterface-V%201.2.0.ipynb
```

```
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSS?*+;;;;;;;+?%SSSSSSS%**%SSSSSSSSSS?**%SSSSSSSSS%?+;;;;;+*%SSSSSSS%*+;;;;+?SSSSSSS%*;;;;;*?SSSSSS
SSSS:..:;;;;;:,.,;%SSSSS+..+SSSSSSSSSS;..+SSSSSS%*:..,;;;;;,..+SSSS%;,.:;;;;,.;SSSS?:..:;;;:,.*SSSSS
SSSS:..?#SSSSSS+..:SSSSS*..+SSSSSSSSSS;..+SSSSS*,.,+%SSSSSSS%++SSS%,.,?SSSSSS??SSS?,.:%SSSSSS?%SSSSS
SSSS:..?#SSSSS#?..:SSSSS*..+SSSSSSSSSS;..+SSSS*..:%SSSSSSSSSSSSSSS?..,?SSSSSSSSSSS*..:%SSSSSSSSSSSSS
SSSS:..+%%%%?*+,,;%SSSSS*..+SSSSSSSSSS;..+SSS%,.,%SSSSSSSSSSSSSSSSS+...:+?%SSSSSSSS;...:+?%SSSSSSSSS
SSSS:..,,,,,,...,*%SSSSS*..+SSSSSSSSSS;..+SSS?..:SSSSSS;,,,,,,,,*SSS?+:,...:;?SSSSSS?+:...,:+?SSSSSS
SSSS:..*%%%%%%?+,.,*SSSS*..+SSSSSSSSSS;..+SSS%,.,%SSSSS?*****,..+SSSSSS%?+;,..:?SSSSSSS%?+:,..:%SSSS
SSSS:..?#SSSSSS#*..:SSSS?..:S#SSSSSS#%:..?SSSS*..:%SSSSSSSS#S:..*SSSSSSSSSSS+..;SSSSSSSSSSS%;..+SSSS
SSSS:..*#SSSSSS?:..*SSSSS+..:*%SSSS%*:..+SSSSSS*,.,+%SSSSSSS%:..+#?+?%SSSSS%;..+SS?+?%SSSSS%:.,*SSSS
SSSS:..,:;;;::,.,:?SSSSSSS?;,..,,,,..,;?SSSSSSSS%*:..,:;;;;:..,;%S?:.,,:;;:,.:*SSS?,.,,:;::.,;?SSSSS
SSSS%?**++++++*?%SSSSSSSSSSS%?*++++*?%SSSSSSSSSSSSS%?+;;;;;+*%SSSSSS%?*++++?%SSSSSSS%?*+++*?%SSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```
