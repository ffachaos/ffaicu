sub hissatu{
	if ($waza_ritu > int(rand(120))) {
		$dmg1 += ($chara[8] + $chara[33]) * int(rand(360));
		$hpplus1 = int($dmg1 / 10);
		$com1 .= "<font class=\"dark\" size=4>�K�E�Z�I�I�_�[�N�E�C�����[�W�����I�I�I</font><br>";
		$kaihuku1 .= "$kname �̂g�o�� $hpplus1 �񕜂����I��";
	}
}
sub atowaza{}
1;