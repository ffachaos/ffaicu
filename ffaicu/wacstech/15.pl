sub wacskouka{
	if (int(rand(10))==0) {
		$com2 .= "<font class=\"dark\" size=3>$winner[27]��������I�I�f�W�����̌��ʁI�I</FONT><br>";
		if (int(rand(3)) == 0) {
			$sake1 -= 999999;
			$dmg2 = $chara[16];
			$com2 .= "<font class=\"yellow\" size=5>���󖂖@�f�W�����I�I�I</FONT><br>";
		} else {
			$com2 .= "<font class=\"red\" size=5>���󖂖@�f�W�����I�I�I���s�����B�B</FONT><br>";
		}
	}
}
1;