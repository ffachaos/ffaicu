sub hissatu{
	if ($waza_ritu > int(rand(120))) {
		$dhit = int(rand(15)) + 1;
		$dmg1 += ($chara[7] + $chara[12]) * int(rand(80));
		$dmg1 = $dmg1 * $dhit;
		$sake2 -= 999999;
		$com1 .= "<font class=\"white\" size=5>�K�E�Z�I�I�I�G���h�E�I�u�E�n�[�g�I�I�I</font><font class=small>$dhit�A���q�b�g�I�I</font><br>";
	}
}
sub atowaza{}
1;