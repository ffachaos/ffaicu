sub hissatu{
	if ($waza_ritu > int(rand(80))) {
		$hpplus1 = ($chara[13] + $chara[33]) + int(rand($chara[20]));
		$dmg1 = 0;
		$com1 .="<font class=\"white\" size=5>$chara[4]�͉񕜂̉̂��̂�����</font><br>";
		$kaihuku1 .= "$chara[4] �̂g�o�� $hpplus1 �񕜂����I��";
	}
}
sub atowaza{}
1;