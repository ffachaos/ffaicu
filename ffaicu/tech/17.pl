sub hissatu{}
sub atowaza{
	if ($waza_ritu > int(rand(120))) {
		if ($mode eq 'isekai' or $mode eq 'boss') {
			$com2 .="<font class=\"red\" size=5>�Ԗ��@�E�I�[���I�I�I</FONT>$mname�ɂ͌����Ȃ������I�I<br>";
		} else {
			$sake1 += 999;
			$dmg2 = 0;
			$com1 .="<font class=\"white\" size=5>�Ԗ��@�E�I�[���I�I�I�i�S�Ă̍U���𖳌��j</font><br>";
		}
	}
}
1;