sub hissatu{
	if ($waza_ritu > int(rand(80))) {
		$dhit = int(rand(7)) + 1;
		$dmg1 = $dmg1 * $dhit;
		$com1 .= "<font class=\"yellow\" size=4>���g�̏p�I�I</font><font color=red>$dhit�̂̕��g����ĂɍU���I�I</font><br>";
	}
}
sub atowaza{}
1;