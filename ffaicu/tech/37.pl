sub hissatu{
	if ($waza_ritu > int(rand(120))) {
		$dhit = int(rand(7)) + 1;
		$dmg1 = $dmg1 * $dhit;
		$com1 .="<font class=\"yellow\" size=4>�K�E�Z�I�I�I���������I�I�I</font><font class=small>$dhit�A���q�b�g�I�I</font><br>";
	}
}
sub atowaza{}
1;