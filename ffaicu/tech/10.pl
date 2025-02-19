sub hissatu{
	if ($waza_ritu > int(rand(120))) {
		$temp_gold =  int(rand($gold)) + 1;
		$com1 .="<font class=\"yellow\">お金を盗んだ♪合計$temp_goldＧゲット♪</font><br>";
		$gold += $temp_gold;
	}
}
sub atowaza{}
1;