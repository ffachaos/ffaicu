sub whissatu{
	if ($wwaza_ritu > int(rand(200))) {
		$dmg2 = 0;
		$hpplus2 = (($winner[12] + $winner[39]) + int(rand($winner[13])))/10;
		$com2 .= "<font class=\"yellow\" size=3>$winner[3]は回復の歌を歌った♪</FONT><br>";
		$kaihuku2 .= "$winner[3] のＨＰが $hpplus2 回復した！♪";
	}
}
sub watowaza{}
1;