sub hissatu{
	if ($waza_ritu > int(rand(80))) {
		$dhit = int(rand(15))+1 * 2;
		$dmg1 = ($chara[8] + $chara[33]) * int(rand(20));
		$dmg1 = $dmg1 * $dhit;
		$sake2 -= 999999;
		$com1 .="<font class=\"yellow\" size=5>�Ñ㖂�@�v���e�I�I�I�I</font><font class=small>$dhit�A���q�b�g�I�I</font><br>";
	}
}
sub atowaza{}
1;