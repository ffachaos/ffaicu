sub hissatu{
	if ($waza_ritu > int(rand(120))) {
		$dhit = int(rand(7)) + 1;
		$dmg1 += ($chara[7] + $chara[33]) * int(rand(10));
		$dmg1 = $dmg1 * $dhit;
		$sake2 -= 999999;
		$com1 .="<font class=\"white\" size=5>�K�E�Z�I�I�I�������_�e�a�I�I�I</font><font class=small>$dhit�A���q�b�g�I�I</font><br>";
	}
}
sub atowaza{}
1;