sub hissatu{
	if ($waza_ritu > int(rand(80))) {
		$sake2 -= 999999;
		$dmg1 = ($chara[8] + $chara[33]) * int(rand(50));
		$com1 .="<font class=\"red\" size=5>黒魔法ファイガ！！！</font><br>";
	}
}
sub atowaza{}
1;