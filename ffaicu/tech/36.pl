sub hissatu{
	if ($waza_ritu > int(rand(80))) {
		$dmg1 += ($chara[7] + $chara[11] + $chara[12] + $chara[33]) * int(rand(80));
		$com1 .="<font class=\"yellow\" size=6>$chara[4]は大きな気の塊を$mname $winner[3]に放った！！</font><br>";
	}
}
sub atowaza{}
1;