sub hissatu{
	if ($waza_ritu > int(rand(120))) {
		$dhit = int(rand(11))+1;
		$sake2 -= 999999;
		$dmg1 = ($chara[8] + $chara[9] + $chara[33]) * int(rand(100));
		$dmg1 = $dmg1 * $dhit;
		$com1 .="<font class=\"yellow\" size=4>���b�i�C�c�E�I�u�E���E���h�����ҁI�I</font><font color=red>$dhit�l�̋R�m���͂�݂����I�I</font><br>";
	}
}
sub atowaza{}
1;