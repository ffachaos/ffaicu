sub acskouka{
	if (int(rand(10))==0) {
		$com1 .= "<font class=\"dark\" size=3>$item[6]��������I�I�f�W�����̌��ʁI�I</font><br>";
		if (int(rand(3)) == 0) {
			$sake2 -= 999999;
			$dmg1 = $winner[16] + $mhp_flg;
			$com1 .= "<font class=\"yellow\" size=5>���󖂖@�f�W�����I�I�I</font><br>";
		} else {
			$com1 .= "<font class=\"red\" size=5>���󖂖@�f�W�����I�I�I���s�����B�B</font><br>";
		}
	}
}
1;