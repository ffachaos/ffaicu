sub hissatu{
	if ($waza_ritu > int(rand(120))) {
		$dmg1+= (($chara[11]+$chara[33]) * int(rand(50)));
		$com1 .="<font class=\"yellow\" size=5>�K�E�Z���C�t�E�f�W�����I�I�I</font><br>";
		$hpplus1 = int($dmg1 / 5);
		$kaihuku1 .= "$chara[4] �̂g�o�� $hpplus1 �񕜂����I��<br>";
	}
}
sub atowaza{}
1;