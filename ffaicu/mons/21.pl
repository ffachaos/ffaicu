sub mons_waza{
	if ($mons_ritu > int(rand(100))) {
		$sake1 -= 999999;
		$ksex = int(rand(2));
		if ($ksex == 1) { $seibetu = "�j"; }
		elsif ($ksex == 0) { $seibetu = "��"; }
		$com2 .= "<font class=\"red\" size=5>���]���I�I�I</font><font color =#cc6633 size = 2><br>���ʂ������_���ɕω�����I$seibetu�ɂȂ����I</font><br>";
	}
}
sub mons_atowaza{}
1;