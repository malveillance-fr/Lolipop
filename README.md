![image](https://github.com/user-attachments/assets/2c01e61a-85ec-44cf-97e6-2b8415b07399)



# Lolipop Tool 🍭

## Description
Lolipop is an easy-to-use, dynamic command-line tool that provides detailed information about IP addresses using multiple external APIs. Whether you want to retrieve data about your own IP address or look up any other IP, Lolipop has you covered. With a colorful and engaging terminal interface powered by the `pystyle` library, you can get IP information in a visually appealing and user-friendly way.

## Features ✨
- **View your IP information**: 
   - Use the command `lolipop -l` to instantly grab detailed information about your public IP address.
   - This includes details like location, organization, and more.
  
- **Look up an IP**: 
   - Use the command `lolipop -i <ip>` to search for detailed information about a specific IP address.
   - This will provide data on the IP’s location, hostname, and other relevant details.
  
- **Multiple API integrations**: 
   - Information is fetched from several popular IP information APIs like `ipinfo.io`, `ip-api.com`, `ipwho.is`, and others.
   - Lolipop uses these APIs to give you a comprehensive view of any given IP.
  
- **Dynamic display**: 
   - The tool displays the gathered information in an organized, visually appealing way using color-coded outputs.
   - The interface is built to be engaging and easy to follow, ensuring a smooth user experience.
  
## Requirements ⚙️
To run Lolipop Tool, you need the following:
- Python 3.x
- `requests` library
- `pystyle` library

### Installation
You can install the required libraries using the following commands:

```bash
pip install requests pystyle

