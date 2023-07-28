/* jshint indent: 2 */

module.exports = function(sequelize, DataTypes) {
  return sequelize.define('metadata', {
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
    setnumber: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    seriesuid: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    collection_: {
      type: DataTypes.STRING(20),
      allowNull: true
    },
    thirdpartyanalysis: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    datadescriptionuri: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    subjectid: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    studyuid: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    studydescription: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    studydate: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    seriesdescription: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    manufacturer: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    modality: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    sopclassname: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    sopclassiod: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    numberofimages: {
      type: DataTypes.STRING(30),
      allowNull: true
    },
    filesize: {
      type: DataTypes.STRING(100),
      allowNull: true
    },
    filelocation: {
      type: DataTypes.STRING(200),
      allowNull: true
    },
    downloadtimestamp: {
      type: DataTypes.STRING(30),
      allowNull: true
    },
    unkown1: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    unkown2: {
      type: DataTypes.STRING(10),
      allowNull: true
    },
    numberofimagesi: {
      type: DataTypes.INTEGER(11),
      allowNull: true
    },
    sigsha: {
      type: DataTypes.STRING(60),
      allowNull: true
    }
  }, {
    sequelize,
    tableName: 'metadata'
  });
};
