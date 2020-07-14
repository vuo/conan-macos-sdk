from conans import ConanFile, tools
import shutil

class MacosSdkConan(ConanFile):
    name = 'macos-sdk'

    sdk_version = '10.11'
    package_version = '0'
    version = '%s-%s' % (sdk_version, package_version)

    settings = 'os'
    url = 'https://developer.apple.com/'
    description = 'macOS SDK'
    sdk_dir = '/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX%s.sdk' % sdk_version

    def package(self):
        self.copy('*', src=self.sdk_dir, symlinks=True, excludes=[
            'System/Library/Frameworks/JavaVM.framework/Versions/A/Resources/Documentation',
            'System/Library/Frameworks/Ruby.framework',
            'usr/bin/*-config',
            'usr/include/apache2',
            'usr/include/apr-1',
            'usr/include/cups',
            'usr/include/curl',
            'usr/include/libxml2',
            'usr/include/libxslt',
            'usr/include/net-snmp',
            'usr/include/nfs',
            'usr/include/php',
            'usr/include/python*',
            'usr/include/tidy',
            'usr/lib/libATCommandStudio.a',
            'usr/lib/libapr*',
            'usr/lib/libhunspell*',
            'usr/lib/libnetsnmp*',
            'usr/lib/libpython*',
            'usr/lib/libruby*',
            'usr/lib/php',
            'usr/lib/python*',
            'usr/lib/ruby',
            'usr/share/man',
        ])
