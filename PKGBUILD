pkgname=python-pm
pkgver="1.0"
pkgrel=1
arch=('any')
license=('MIT')
depends=('python')
install=pm.install
source=('pm-monitor'
		'pm-monitor.service'
		'pm-reportemail'
		'pm-reportemail.service'
		'pm-reportemail.timer'
		'LICENSE')
md5sums=('bbb4fb4044e3e148191c9893bd7839cf'
         'c321fc892f4ade6ba2387d4d39a2125e'
         'd967ff3fd0e51bfd19b5a81b78d2acb1'
         '775d704e730a22288bc0a96d22983565'
         '9aaf4256165b4c2897895a896d569842'
         'a070c56a534bd24b360cf374d8114df1')
package() {
	install -Dm755 $srcdir/pm-monitor $pkgdir/usr/bin/pm-monitor
	install -Dm755 $srcdir/pm-reportemail $pkgdir/usr/bin/pm-reportemail

	install -Dm644 $srcdir/pm-monitor.service $pkgdir/etc/systemd/system/pm-monitor.service
	install -Dm644 $srcdir/pm-reportemail.service $pkgdir/etc/systemd/system/pm-reportemail.service
	install -Dm644 $srcdir/pm-reportemail.timer $pkgdir/etc/systemd/system/pm-reportemail.timer

	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
