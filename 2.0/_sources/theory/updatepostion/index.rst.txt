颗粒位置的更新
==============



得到某颗粒在时刻 :math:`t` 所受合力后，就可以更新颗粒的位置和角速度 。根据牛顿第二运动定律有：

.. math:: \vec{a_t}=\vec{F_t}/m

.. math:: \eta_t=M_t/I

其中，:math:`\vec{a_t}` 和 :math:`\eta_t` 分别表示颗粒在时刻 :math:`t` 的平动加速度和角加速度， :math:`\vec{F_t}` 和 :math:`M_t` 分别为颗粒在该时刻的合力和合力矩，:math:`m` 和 :math:`I` 分别为颗粒的质量和惯性矩。

假设已知某颗粒在 :math:`\eta_t` 时的位置 :math:`\vec{P_t}` 和 :math:`t-\bigtriangleup{t}` 平动加速度 :math:`\overrightarrow{v_{t-\bigtriangleup{t}/2}}` 时的平动速度，则按照跳蛙法有， 

.. math:: \overrightarrow{v_{t+\bigtriangleup{t}/2}}=\overrightarrow{v_{t-\bigtriangleup{t}/2}}+\vec{a_t}\cdot\bigtriangleup{t}

.. math:: \overrightarrow{P_{t+\bigtriangleup{t}}}=\overrightarrow{P_{t}}+\overrightarrow{v_{t+\bigtriangleup{t}/2}}\cdot\bigtriangleup{t}

其中，:math:`\bigtriangleup{t}` 为一个时步。 


首先，得到颗粒在 :math:`t+\bigtriangleup{t}/2` 时的速度 :math:`\overrightarrow{v_{t+\bigtriangleup{t}/2}}` ，再得到颗粒在 :math:`t+\bigtriangleup{t}` 时的位置 :math:`\overrightarrow{v_{t+\bigtriangleup{t}/2}}`。之后，由相应的接触力学模型计算颗粒间的接触力，得到 :math:`t+\bigtriangleup{t}` 时颗粒所受合力，通过牛顿第二运动定律求得 :math:`t+\bigtriangleup{t}` 的颗粒的平动加速度，就可以更新颗粒 :math:`t+\bigtriangleup{t}` 时的位置，这样一直迭代循环下去，直到计算结束。 

同理，假设某颗粒在 :math:`t` 时的角度为 :math:`\theta_{t}` 和角加速度为 :math:`\eta_t` ，:math:`t-\bigtriangleup{t}/2` 时的角速度为 :math:`\omega_{t-\bigtriangleup{t}/2}` ，则按照跳蛙法有，

.. math:: \omega_{t+\bigtriangleup{t}/2}=\omega_{t-\bigtriangleup{t}/2}+\eta_t\cdot\bigtriangleup{t}

.. math:: \theta_{t+\bigtriangleup{t}}=\theta_{t}+\omega_{t+\bigtriangleup{t}/2}\cdot\bigtriangleup{t}


在接触力学模型部分， 颗粒所受切向力一般由位移增量（颗粒在接触点处的相对速度 :math:`\times\bigtriangleup{t}` ）计算得到，不需要颗粒的角度值。如果没有其它特殊需要，可以不更新颗粒的角度，只更新颗粒的角速度即可。


