sub hissatu{
	if ($waza_ritu > int(rand(100))) {
		$com1 .= "<font color=\"$white\">$chara[4]�́A�^���b�g�J�[�h���ꖇ�������I�I ���������H �S�Ă͂��̉^���̃J�[�h�ꖇ�Ɉς˂�ꂽ�b�I�I</font><br>";
		$ura = int(rand(22));
		if (0 == $ura) {
			$com1 .= "THE MAGICIAN�I�I�I�I\n";
			$dmg1 += ($chara[8] + $chara[9]) * int(rand(80));
			$sake2 -= 999999;
		} elsif (1 == $ura) {
			$com1 .= "THE CHARIOT�I�I�I�I\n";
			$dmg1 += ($chara[7] + $chara[11]) * int(rand(80));
			$sake2 -= 999999;
		} elsif (2 == $ura) {
			$com1 .= "STRENGTH�I�I�I\n";
			$dmg1 += ($chara[7] + $chara[10]) * int(rand(80));
			$sake2 -= 999999;
		} elsif (3 == $ura) {
			$com1 .= "THE HIGH PRIESTESS�I�I�I\n";
			$dmg1 = 0;
			$hpplus1 = ($chara[8] + $chara[9]) * int(rand(180));
			$kaihuku1 .= "$chara[4] �̂g�o�� $hpplus1 �񕜂����I��";
		} elsif (4 == $ura) {
			$com1 .= "THE HIEROPHANT�I�I�I�I\n";
			$dmg1 += ($chara[7] +$chara[8] + $chara[9]) * int(rand(80));
			$sake2 -= 999999;
		} elsif (5 == $ura) {
			$com1 .= "THE EMPRESS�I�I�I�I\n";
			$dmg1 += ($chara[7] +$chara[8] + $chara[9]) * int(rand(120));
			$sake2 -= 999999;
		} elsif (6 == $ura) {
			$com1 .= "THE EMPEROR�I�I�I�I�I\n";
			$dmg1 += ($chara[7] +$chara[8] + $chara[9]) * int(rand(180));
			$sake2 -= 999999;
		} elsif (7 == $ura) {
			$com1 .= "THE LOVERS�I�I�I�I\n";
			$hpplus1 = $chara[10] * int(rand(80));
			$dmg1 = 0;
			$kaihuku1 .= "$chara[4] �̂g�o�� $hpplus1 �񕜂����I��";
		} elsif (8 == $ura) {
			$com1 .= "THE HERMIT�I�I�I�I\n";
			$dmg1 += $chara[13] * int(rand(80));
			$sake2 -= 999999;
		} elsif (9 == $ura) {
			$com1 .= "WHEEL of FORTUNE�I�I�I�I\n";
			$dmg1 = ($chara[7] +$chara[8] + $chara[9] + $chara[10] +$chara[11] + $chara[12] + $chara[13]) * int(rand(80));
			$sake2 -= 999999;
		} elsif (10 == $ura) {
			$com1 .= "JUSTICE�I�I�I�I\n";
			$dmg1 += ($chara[7] + $chara[9] ) * int(rand(180));
			$sake2 -= 999999;
		} elsif (11 == $ura) {
			$com1 .= "THE HANGEDMAN�I�I�I�I\n";
			$dmg1 = int(0);
		} elsif (12 == $ura) {
			$com1 .= "DEATH�I�I�I�I\n";
			$dmg1 = $whp_flg + $mhp + $wd_dmg;
			$sake2 -= 999999;
		} elsif (13 == $ura) {
			$com1 .= "TEMPERANCE�I�I�I�I\n";
			$dmg1 = ($chara[7] +$chara[8] + $chara[9] + $chara[10] +$chara[11] + $chara[12] + $chara[13]) * int(rand(80));
			$sake2 -= 999999;
		} elsif (14 == $ura) {
			$com1 .= "THE DEVIL�I�I�I�I\n";
			$dmg1 = 0;
			$dmg2 = $khp_flg;
			$sake1 -= 999999;
		} elsif (15 == $ura) {
			$com1 .= "THE TOWER�I�I�I�I\n";
			$hpplus2 = ($chara[7] +$chara[8] + $chara[9] + $chara[10] +$chara[11] + $chara[12] + $chara[13]) * int(rand(180));
			$dmg1 = 0;
			$kaihuku2 .= "$winner[3] �̂g�o�� $hpplus2 �񕜂����I��";
		} elsif (16 == $ura) {
			$com1 .= "THE STAR�I�I�I�I\n";
			$dmg1 += ($chara[9] + $chara[13]) * int(rand(80));
		} elsif (17 == $ura) {
			$com1 .= "THE MOON�I�I�I�I\n";
			$hpplus1 = ($chara[8] + $chara[9]) * int(rand(80));
			$dmg1 = 0;
			$kaihuku1 .= "$chara[4] �̂g�o�� $hpplus1 �񕜂����I��";
		} elsif (18 == $ura) {
			$com1 .= "THE SUN�I�I�I�I\n";
			$dmg1 += ($chara[7] + $chara[11]) * int(rand(999));
			$sake2 -= 999999;
		} elsif (19 == $ura) {
			$com1 .= "THE JUDGEMENT�I�I�I�I\n";
			$dmg1 += ($chara[8] + $chara[9]) * int(rand(999));
			$sake2 -= 999999;
		} elsif (20 == $ura) {
			$com1 .= "THE WORLD�I�I�I�I\n";
			$dmg1 = ($chara[7] +$chara[8] + $chara[9] + $chara[10] +$chara[11] + $chara[12] + $chara[13]) * int(rand(80));
			$sake2 -= 999999;
		} else{
			$com1 .= "THE FOOL\n";
			$dmg1 = int(1);
		}
	}
}
sub atowaza{}
1;