sub wacskouka{
	if (int(rand(30))==1) {
		if ($whp_flg < $dmg1) {
			if ($wa_22lmt >= 3) {
				$winner[51] == 0;
				$com2 .= "<font class=\"green\" size=3>$winner[27]�͌���Ȃ������B�B�B</FONT><br>";
			} else {
				$wa_22lmt++;
				$dmg2 += $dmg1;
				$dmg1 = 0;
				$com2 .= "<font class=\"white\" size=3>$winner[27]��������I�I$chara[4]�̍U���𒵂˕Ԃ����I�I</FONT><br>";
			}
		}
	}
}
1;