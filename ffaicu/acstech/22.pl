sub acskouka{
	if (int(rand(10))==0) {
		if ($khp_flg < $dmg2) {
			if ($a_22lmt >= 3) {
				$com1 .= "<font class=\"red\" size=3>$item[6]�͌���Ȃ������B�B�B</font><br>";
			} else {
				$a_22lmt++;
				$dmg1 += $dmg2;
				$dmg2 = 0;
				$com1 .= "<font class=\"white\" size=3>$item[6]��������I�I$winner[3] $mname�̍U���𒵂˕Ԃ����I�I</font><br>";
			}
		}
	}
}
1;