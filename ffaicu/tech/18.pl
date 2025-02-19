sub hissatu{
	if ($waza_ritu > int(rand(80))) {
		$hpplus1 = ($chara[13] + $chara[33]) + int(rand($chara[20]));
		$dmg1 = 0;
		$com1 .="<font class=\"white\" size=5>$chara[4]は回復の歌を歌った♪</font><br>";
		$kaihuku1 .= "$chara[4] のＨＰが $hpplus1 回復した！♪";
	}
}
sub atowaza{}
1;