sub hissatu{}
sub atowaza{
	if ($waza_ritu > int(rand(120))) {
		$sake1 += 999;
		$sake2 -= 999999;
		$dmg1+= (($chara[7] + $chara[11] + $chara[33]) * int(rand(160)));
		$com1 .="<font class=\"white\" size=5>旋空飛竜滅殺槍！！</font><br>";
	}
}
1;