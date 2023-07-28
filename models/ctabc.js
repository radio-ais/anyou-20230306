/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('ctabc', {
    id: {
      autoIncrement: true,
      type: DataTypes.BIGINT,
      allowNull: false,
      primaryKey: true
    },
    createdat: {
      type: DataTypes.DATE,
      allowNull: true,
      defaultValue: sequelize.fn('current_timestamp')
    },
    updatedat: {
      type: DataTypes.DATE,
      allowNull: true
    },
    study_yr: {
      type: DataTypes.STRING(40),
      allowNull: true
    },
    sct_ab_preexist: {
      type: DataTypes.STRING(40),
      allowNull: true
    },
    pid: {
      type: DataTypes.STRING(40),
      allowNull: true
    },
    sct_ab_attn: {
      type: DataTypes.STRING(40),
      allowNull: true
    },
    sct_ab_gwth: {
      type: DataTypes.STRING(40),
      allowNull: true
    },
    sct_ab_invg: {
      type: DataTypes.STRING(40),
      allowNull: true
    },
    sct_ab_num: {
      type: DataTypes.STRING(40),
      allowNull: true
    },
    sct_ab_code: {
      type: DataTypes.STRING(40),
      allowNull: true
    },
    dataset_version: {
      type: DataTypes.STRING(40),
      allowNull: true
    },
    visible_days: {
      type: DataTypes.STRING(40),
      allowNull: true
    }
  }, {
    sequelize,
    tableName: 'ctabc'
  });
};
