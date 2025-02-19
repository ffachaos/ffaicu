sub hissatu{
	if ($waza_ritu > int(rand(80))) {
		$dmg1 += ($chara[7] + $chara[33]) * int(rand(50));
		$com1 .="<font class=\"red\" size=5>必殺技凶斬り！！！</font><br>";
	}
}
sub atowaza{}
1;