sub mons_waza{
	if ($mons_ritu > int(rand(100))) {
		$sake1 -= 999999;
		$dmg2 += int(rand($mrand)) * 3;
		$dmg2 += $item[4];
		$com2 .= "<font class=\"white\" size=5>�֒f�̖��@�A���e�}�𔭓��I�I�I</font><br>";
	}
}
sub mons_atowaza{}
1;