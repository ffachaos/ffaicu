sub hissatu{
	if ($waza_ritu > int(rand(80))) {
		$dmg1 += ($chara[7] + $chara[11] + $chara[12] + $chara[33]) * int(rand(80));
		$com1 .="<font class=\"yellow\" size=6>$chara[4]�͑傫�ȋC�̉��$mname $winner[3]�ɕ������I�I</font><br>";
	}
}
sub atowaza{}
1;