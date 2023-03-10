<h1>Convert your VCF contacts to CSV with ease! 📱💻</h1>
<p>Do you want to have a simple CSV backup of your contacts, but dread doing it manually? Look no further! This script easily converts your phone's contacts to CSV, making it easy for you to store and access your contacts in a human-readable format. Works for both Android and iOS.</p>
<h2>Table of Contents</h2>
<ol>
  <li><a href="#obtaining-the-vcf-file" target="_new">Obtaining the VCF file</a>
    <ol>
      <li><a href="#android" target="_new">Obtaining the VCF file on Android</a></li>
      <li><a href="#ios" target="_new">Obtaining the VCF file on iOS</a></li>
    </ol>
  </li>
  <li><a href="#prerequisites" target="_new">Prerequisites</a></li>
  <li><a href="#installation" target="_new">Installation</a></li>
  <li><a href="#usage" target="_new">Usage</a></li>
  <li><a href="#troubleshooting" target="_new">Troubleshooting</a></li>
</ol>
<h2>Obtaining the VCF file 📱</h2>
<p>In order to convert your contacts to a CSV file, you will need to first export your contacts to a VCF file. Here's how you can do that on both Android and iOS devices:</p>
<h3>Android</h3>
<ol>
  <li>Open the "Contacts" app on your Android device.</li>
  <li>Tap the three vertical dots in the top right corner of the screen to open the menu.</li>
  <li>Select "Manage contacts".</li>
  <li>In the Manage Contacts menu, select "Export contacts".</li>
  <li>Choose "All contacts" (or seelct the ones you want) and as the destination, select "Internal storage". Press "Export".</li>
  <li>Then, head over to the standard "Files" app on Android.</li>
  <li>Enter "Contacts.vcf" in the search bar or go to "Internal Storage" and search for it there.</li>
  <li>Once the file is displayed, press it for a few seconds, then select "Share" and there, select some email service (sharing via social media often only exports the first contact). Send it to yourself so that you can access it on your computer.</li>
</ol>
<h3>iOS</h3>
<ol>
  <li>Haven't checked that yet in detail, <a href="https://www.gadgetgone.com/blog/export-contacts-from-iphone/">here</a> is a link to a page that shows how it should work. </li>
</ol>
<h2>Prerequisites</h2>
<p>Before getting started, you will need:</p>
<ul>
  <li>Python 3 installed on your computer, download <a href="https://www.python.org/downloads/">here</a></li>
  <li>The "Contacts.vcf" (name doesn't matter) file you exported from your phone.</li>
  <li>(Of course, Git: Install via <a href="https://formulae.brew.sh/formula/git">Homebrew</a> on Mac (might need to install Homebrew itself first) and <a href="https://gitforwindows.org/">Git for Windows</a> on Windows)</li>
</ul>
<h2>Installation</h2>
<ol>
  <li>On Mac: Open a Terminal window on Mac (or a cmd or Powershell window on Windows) and go to the directory you want the project to be in, first get an overview over the directories typing <code>pwd</code> and then switch to the directory of your choice, e.g. to Documents with <code>cd Documents</code>.</li>
  <li>Clone this repository with <code>git clone https://github.com/KensingtonOscupant/phone-contacts-to-csv.git'.</code></li>
  <li>Still in your Terminal/Powershell window, move switch to the project directory with <code>cd phone-contacts-to-csv</code>.</li>
  <li>Move your "Contacts.csv" file into the phone-contacts-to-csv folder you are in through the Finder or File Explorer.</li>
</ol>
<h2>Usage</h2>
<ol>
  <li>In the command line, run the script by typing <code>python convert.py &lt;Contacts.csv&gt;</code>, where <code>&lt;Contacts.csv&gt;</code> is the name of your contacts file.
    <ul>
      <li>Example: <code>python convert.py Contacts.vcf</code></li>
    </ul>
  </li>
  <li>The script will create a new CSV file with the same name as your VCF file in the same directory.</li>
  <li>You can open the CSV file in a program such as Microsoft Excel or Google Sheets to view and edit your contacts.</li>
</ol>
<h2>Troubleshooting</h2><ul><li><strong>File not found error</strong>: Make sure the file path of your VCF file is correct and that the file exists in the specified location.</li></ul><p>If you have any issues or questions, please feel free to create an issue in this repository and we will be happy to help you out! 🤗</p>
