sub hissatu{}
sub atowaza{
	if ($waza_ritu > int(rand(120))) {
		if ($mode eq 'isekai' or $mode eq 'boss') {
			$com1 .="<font class=\"yellow\" size=5>���󖂖@�X�g�b�v�I�I�I</FONT>$mname�ɂ͌����Ȃ������I�I<br>";
		} else {
			$sake2 -= 999999;
			$dmg2 = 0;
			$com1 .="<font class=\"yellow\" size=5>���󖂖@�X�g�b�v�I�I�I</font>$winner[3] $mname�̓������~�߂��I<br>";
		}
	}
}
1;