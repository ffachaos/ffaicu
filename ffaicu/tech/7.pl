sub hissatu{
	if ($waza_ritu > int(rand(120))) {
		$dmg1 = 0;
		$hpplus1 = ($chara[9] + $chara[33]) + int(rand($chara[20]));
		$com1 .="<font class=\"white\" size=5>�����@�P�A���K�I�I�I</font><br>";
		$kaihuku1 .= "$chara[4] �̂g�o�� $hpplus1 �񕜂����I��";
	}
}
sub atowaza{}
1;