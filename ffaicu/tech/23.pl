sub hissatu{}
sub atowaza{
	if ($waza_ritu > int(rand(120))) {
		if ($mode eq 'isekai' or $mode eq 'boss') {
			$com1 .="<font class=\"yellow\" size=4>���b�J�[�o���N�������ҁI�I���t���N�I�I</FONT>$mname�ɂ͌����Ȃ������I�I<br>";
		} else {
			$dmg1 += $dmg2;
			$dmg2 = 0;
			$com1 .="<font class=\"yellow\" size=4>���b�J�[�o���N�������ҁI�I���t���N�I�I�i�U���𔽎ˁj</font><br>";
		}
	}
}
1;