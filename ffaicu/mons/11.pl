sub mons_waza{
	if ($mons_ritu > int(rand(100))) {
		if (int(rand(3))==0) {
			$sake1 -= 999999;
			$dmg2 = $khp_flg;
			$dmg2 += $item[4];
			$com2 .= "<font class=\"red\" size=5>���󖂖@�f�W�����𔭓��I�I�I</font><br>";
		} else {
			$com2 .= "<font class=\"red\" size=5>���󖂖@�f�W�����𔭓��I�I�I���s�I�I</font><br>";
		}
	}
}
sub mons_atowaza{}
1;