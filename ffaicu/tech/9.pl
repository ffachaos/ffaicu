sub hissatu{}
sub atowaza{
	if ($waza_ritu > int(rand(80))) {
		if ($mode eq 'isekai' or $mode eq 'boss' && int(rand(4)) == 1) {
			$com1 .= "$chara[4]�����񂾁I<font size=5>�u���I����͂Ȃ񂾁I�H�H�H�H�v</font>$winner[3] $mname�ɂ͌����Ȃ������I�I<br>";
		} else {
			$sake2 -= 999999;
			$dmg2 = 0;
			$com1 .="$chara[4]�����񂾁I<font size=5>�u���I����͂Ȃ񂾁I�H�H�H�H�v</font>$winner[3] $mname�Ɍ����ł����I<br>";
		}
	}
}
1;