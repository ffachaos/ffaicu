sub mons_waza{
	if ($mons_ritu > int(rand(100))) {
		$dmhit = int(rand(7))+1;
		$sake1 -= 999999;
		$dmg2 = int(rand($mrand)) * $dmhit;
		$dmg2 += $item[4];
		$com2 .= "<font class=\"red\" size=5>�Ñ㖂�@���e�I�I�I�I</font><font color=red>$dmhit�q�b�g�I�I</font><br>";
	}
}
sub mons_atowaza{}
1;