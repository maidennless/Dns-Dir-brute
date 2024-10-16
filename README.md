# Directory and Subdomain Brute Forcer in Python

This Python script is designed to perform brute-forcing on directories and subdomains. It supports two modes: `dir` for directory brute-forcing and `dns` for DNS enumeration (subdomain brute-forcing). The script utilizes multithreading for fast enumeration, making it efficient for large wordlists.

## Features
- **Directory Brute-forcing**: Scans for directories on a given URL.
- **Subdomain Brute-forcing**: Enumerates subdomains on a given domain.
- **Multithreading**: Utilizes Python’s `concurrent.futures` module to speed up the process by running multiple threads concurrently.

## Requirements
- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Requests Library**: Install this library by running `pip install requests` if you haven’t already.

## Usage
Run the script from the command line with the required arguments. Choose the mode (`dir` or `dns`) and specify the wordlist file, along with the target URL or domain.

### Example Usage
```bash
# DNS Enumeration Mode
python brute_force.py dns -w wordlist.txt -d example.com

# Directory Brute-forcing Mode
python brute_force.py dir -w wordlist.txt -u http://example.com

#Example Output
console:
[+] Wordlist: wordlist.txt
[+] URL: http://example.com
http://example.com/admin : 200
http://example.com/login : 200
```

### Disclaimer

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**
